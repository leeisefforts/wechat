from flask import Blueprint, jsonify, request
from common.Helper import WeChatService, xml_to_dict, getCurrentDate, dict_to_xml
from common.libs.followers import FollowerSevice
from common.libs.SignIn import SignInService
from application import db, app
from common.modals.ConversationLog import ConversationLog
import requests, json, time, hashlib

route_auth = Blueprint('wechat_page', __name__)
token = 'meihuomeipu'

testXml = '<xml>  <ToUserName>test</ToUserName>  <FromUserName>oCMdfwKnqFIOhC6FxV3nG9KuEiUA</FromUserName> ' \
          '<CreateTime>1348831860</CreateTime>  <MsgType>text</MsgType>  <Content>' \
          '签到</Content>  <MsgId>1234567890123456</MsgId> </xml>'


@route_auth.route('/authWeChat')
def authWeChat():
    signature = request.values['signature']
    timestamp = request.values['timestamp']
    nonce = request.values['nonce']
    echostr = request.values['echostr']
    tmp = [token, timestamp, nonce]
    tmp.sort()
    tmp = ''.join(tmp)
    return tmp


@route_auth.route('test')
def test():
    return jsonify('tesgfgbbb')


'''

'<xml>  <ToUserName>test</ToUserName>  <FromUserName>oCMdfwKnqFIOhC6FxV3nG9KuEiUA</FromUserName> ' \
          '<CreateTime>1348831860</CreateTime>  <MsgType>text</MsgType>  <Content>' \
          '签到</Content>  <MsgId>1234567890123456</MsgId> </xml>'
'''


@route_auth.route('/wechat_msg', methods=["GET", "POST"])
def wechat_msg():
    signature = request.values['signature']
    timestamp = request.values['timestamp']
    nonce = request.values['nonce']

    tmp = [token, timestamp, nonce]
    tmp.sort()
    tmp = ''.join(tmp)
    tmp = hashlib.sha1(tmp.encode('utf-8')).hexdigest()
    if tmp == signature:
        if request.method == "GET":
            echostr = request.values['echostr']
            return echostr

        xml = request.data
        code = xml_to_dict(xml)
        result = 'success'
        # 判断openid是否存在
        fl_info = FollowerSevice.OpsFlByOpenId(code['FromUserName'])

        if fl_info:

            if code['Content'] == '签到':
                SignInService.opsSign(fl_info)
            else:
                if code['MsgType'] == 'event':
                    if code['Event'] == 'subscribe':
                        FollowerSevice.send_msg(
                            '终于等到你 还好我没放弃\r\n\r\n美货美铺，八年专业海淘经验\r\n您身边值得信任的海淘专家！\r\n晨大人 微信：shijimonian', fl_info.OpenId)

            cl = ConversationLog()
            cl.CreateTime = getCurrentDate()
            cl.ToUserName = code['ToUserName']
            cl.FromUserName = code['FromUserName']
            cl.Content = code['Content']

            db.session.add(cl)
            db.session.commit()

        # tm = int(time.time())
        # result = {
        #     'ToUserName': code['FromUserName'],
        #     'FromUserName': code['ToUserName'],
        #     'CreateTime': tm,
        #     'MsgType': 'text',
        #     'Content': str
        # }
        # result = dict_to_xml(result)

    return result


@route_auth.route('/createmenus', methods=["GET", "POST"])
def createMenus():
    btns = {
        "button": [
            {
                "name": "美货推荐",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "美妆篇",
                        "url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzIyNzUwMjM0NA%3D%3D&hid=1&sn=5ea0ed7382c6fed7653b1bedaf7ac651&scene=18"
                    },
                    {
                        "type": "view",
                        "name": "护肤篇",
                        "url": "https://mp.weixin.qq.com/mp/homepage?__biz=MzIyNzUwMjM0NA%3D%3D&hid=2&sn=89b55554babe3f87fbc15ac0dfa4eb4a&scene=18"
                    }
                ]
            },
            {
                "name": "签到有礼",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "线上美铺",
                        "url": "https://weidian.com/s/974925138"
                    },
                    {
                        "type": "click",
                        "name": "签到有礼",
                        "key": "SignIn"
                    }
                ]
            },
            {
                "name": "关于美货",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "加入我们",
                        "url": "http://a2.rabbitpre.com/m2/aUe1ZjNlQa"
                    },
                    {
                        "type": "view",
                        "name": "商务合作",
                        "url": "http://www.meihuomeipu.com"
                    },
                    {
                        "type": "view",
                        "name": "快递查询",
                        "url": "http://www.xlobo.com/"
                    },
                    {
                        "type": "view",
                        "name": "公司主页",
                        "url": "http://www.meihuomeipu.com"
                    }
                ]
            }
        ]
    }

    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}'.format(WeChatService.getAccessToken())
    data = json.dumps(btns, ensure_ascii=False).encode('utf-8')
    r = requests.post(url, data=data)
    return jsonify(r.text)
