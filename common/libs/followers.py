from application import app, db
from common.modals.Followers import Follower
from common.Helper import WeChatService, getCurrentDate
import requests, json


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
        db.session.add(follower)
        db.session.commit()
        return follower

    @staticmethod
    def send_msg(strd, openId):
        header = {'content-type': "application/json; charset = 'utf-8' "}
        data = {
            "touser": openId,
            "msgtype": "text",
            "text":
                {
                    "content": strd
                }
        }
        url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={0}".format(WeChatService.getAccessToken())
        data = json.dumps(data,ensure_ascii=False).encode('utf-8')
        r = requests.post(url,headers= header, data=data)

        r.text

