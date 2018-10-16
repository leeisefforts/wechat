from flask import Blueprint, jsonify
from common.Helper import WeChatService, xml_to_dict
from common.libs.followers import FollowerSevice
from common.modals.Followers import Follower
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


@route_auth.route('/getAllFollower')
def get_all_followers():
    str = '<xml>  <ToUserName>tousername</ToUserName>  <FromUserName>fromusername</FromUserName>  ' \
          '<CreateTime>1348831860</CreateTime>  <MsgType>test</MsgType>  <Content>' \
          '签到</Content>  <MsgId>1234567890123456</MsgId> </xml>'
    code = xml_to_dict(str)

    # 判断openid是否存在
    fl_info = FollowerSevice.OpsFlByOpenId(code['FromUserName'])

    if fl_info:
        pass

    if code['Content'] == '签到':
        return jsonify(2)

    return jsonify(code['Content'])
