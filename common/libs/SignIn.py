from application import db, app
from common.modals.SignIn import SignIn
from common.Helper import getCurrentDate
import datetime, json
from common.libs.followers import FollowerSevice


class SignInService():

    def __init__(self):
        pass

    @staticmethod
    def opsSign(fl_info):
        si = SignIn.query.filter(SignIn.OpenId == fl_info.OpenId).first()
        strd = ''
        if not si:
            signin = SignIn()
            signin.OpenId = fl_info.OpenId
            signin.SignInDays = 1
            signin.SignInTime = getCurrentDate()
            db.session.add(signin)
            db.session.commit()
            strd = '签到成功, 您已连续签到1天'

            FollowerSevice.send_msg(strd, fl_info.OpenId)
            pass

        date = datetime.datetime.strptime(str(si.SignInTime), '%Y-%m-%d %H:%M:%S')

        # 判断是否在今天
        now = datetime.datetime.now()
        stf = (now - date).seconds
        if stf < 86400:
            strd = '今天您已经签到过了'
        else:

            si.SignInDays += 1
            si.SignInTime = getCurrentDate()
            db.session.add(si)
            db.session.commit()

            strd = '签到成功, 您已连续签到{0}天'.format(si.SignInDays)

        FollowerSevice.send_msg(strd, fl_info.OpenId)

