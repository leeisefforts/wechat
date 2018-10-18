from flask import Blueprint, jsonify, request
from common.Helper import WeChatService, xml_to_dict, getCurrentDate, dict_to_xml
from common.libs.followers import FollowerSevice
from common.libs.SignIn import SignInService
from application import db, app
from common.modals.ConversationLog import ConversationLog
import requests, json, time, hashlib

route_auth = Blueprint('wechat_page', __name__)

@route_auth.route('/authWeChat')
def authWeChat():
    return WeChatService.getAccessToken()

@route_auth.route('/vaild')
def vaild_wechat():
    signature = request.query_string['signature']
    timestamp = request.query_string['timestamp']
    nonce = request.query_string['nonce']
    echostr = request.query_string['echostr']
    tmp = [app.config['APPTOKEN'], timestamp, nonce]
    tmp.sort()
    tmp = ''.join(tmp)
    tmp =  hashlib.sha1(tmp).hexdigest()
    if tmp == signature:
        return echostr

'''

'<xml>  <ToUserName>test</ToUserName>  <FromUserName>oCMdfwKnqFIOhC6FxV3nG9KuEiUA</FromUserName> ' \
          '<CreateTime>1348831860</CreateTime>  <MsgType>text</MsgType>  <Content>' \
          '签到</Content>  <MsgId>1234567890123456</MsgId> </xml>'
'''


@route_auth.route('/wechat_msg')
def wechat_msg():
    xml = request.values
    code = xml_to_dict(xml)
    str = ''
    # 判断openid是否存在
    fl_info = FollowerSevice.OpsFlByOpenId(code['FromUserName'])

    if fl_info:

        if code['Content'] == '签到':
            str = SignInService.opsSign(fl_info)

        cl = ConversationLog()
        cl.CreateTime = getCurrentDate()
        cl.ToUserName = code['ToUserName']
        cl.FromUserName = code['FromUserName']
        cl.Content = code['Content']

        db.session.add(cl)
        db.session.commit()

    tm = int(time.time())
    result = {
        'ToUserName': code['FromUserName'],
        'FromUserName': code['ToUserName'],
        'CreateTime': tm,
        'MsgType': 'text',
        'Content': str
    }
    result = dict_to_xml(result)

    return result
