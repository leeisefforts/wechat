from flask import Blueprint, jsonify
from common.Helper import WeChatService, xml_to_dict, getCurrentDate
from common.libs.followers import FollowerSevice
from common.libs.SignIn import SignInService
from application import db, app
from common.modals.ConversationLog import ConversationLog
import requests, json

route_auth = Blueprint('wechat_page', __name__)


@route_auth.route('/authWeChat')
def authWeChat():
    # url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(
    #     app.config['APPID'], app.config['APPSERCRETID'])
    # res = requests.get(url)
    # res = res.json()
    #
    # account = Account()
    # account.AccountName = '美货美铺'
    # account.AppId = app.config['APPID']
    # account.Created_time = datetime.datetime.now()
    # account.Updated_time = datetime.datetime.now()
    # account.Access_Token = res['access_token']
    # account.Expires_In = res['expires_in']
    #
    # db.session.add(account)
    #
    # db.session.commit()
    return WeChatService.getAccessToken()


'''

<xml>  
<ToUserName>< ![CDATA[toUser] ]></ToUserName>  <FromUserName>< ![CDATA[fromUser] ]>
</FromUserName>  <CreateTime>1348831860</CreateTime>  <MsgType>< ![CDATA[text] ]></MsgType>  
<Content>< ![CDATA[this is a test] ]></Content>  <MsgId>1234567890123456</MsgId>  
</xml>
'''


@route_auth.route('/wechat_msg')
def wechat_msg():
    xml = '<xml>  <ToUserName>test</ToUserName>  <FromUserName>oCMdfwKnqFIOhC6FxV3nG9KuEiUA</FromUserName> ' \
          '<CreateTime>1348831860</CreateTime>  <MsgType>text</MsgType>  <Content>' \
          '签到</Content>  <MsgId>1234567890123456</MsgId> </xml>'
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

    return str
