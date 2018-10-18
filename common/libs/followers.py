from application import app, db
from flask import jsonify
from common.modals.Followers import Follower
from common.Helper import WeChatService, getCurrentDate
import requests


class FollowerSevice():

    @staticmethod
    def OpsFlByOpenId(openId):
        fl_info = None

        fl_info = Follower.query.filter(Follower.OpenId == openId).first()
        if fl_info:
            return fl_info

        url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token={0}&openid={1}&lang=zh_CN'.format(
            WeChatService.getAccessToken(), openId)
        res = requests.get(url)

        fl = res.json()
        follower = Follower()
        follower.CreateTime = getCurrentDate()

        follower.NickName = fl['nickname']
        follower.Sex = fl['sex']
        follower.HeadImgUrl = fl['headimgurl']
        follower.OpenId = fl['openid']
        follower.Language = fl['language']
        follower.Subscribe_time = fl['subscribe_time']
        follower.UpdateTime = getCurrentDate()

        return fl_info

    @staticmethod
    def send_msg(str, openId):
        headers = {'Content-Type': 'application/json'}
        data = {
            "touser": openId,
            "msgtype": "text",
            "text":
                {
                    "content": str
                }
        }
        url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={0}".format(WeChatService.getAccessToken())
        r = requests.post(url, headers=headers, data=jsonify(data))

        r.text

