from common.modals.Followers import Follower
from application import app, db
import datetime, requests
from common.Helper import WeChatService, getCurrentDate


class JobTask():
    def __init__(self):
        pass

    def run(self, ret_params):
        url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token={0}&next_openid='.format(
            WeChatService.getAccessToken())
        res = requests.get(url)

        openIds = res.json()['data']['openid']

        for openId in openIds:
            url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token={0}&openid={1}&lang=zh_CN'.format(
                WeChatService.getAccessToken(), openId)
            res = requests.get(url)

            fl = res.json()
            fl_into = Follower.query.filter(Follower.OpenId == openId).first()

            if fl_into:
                follower = fl_into
            else:
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