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
            strd = '恭喜小可爱签到成功~\r\n您已连续签到1天了！\r\n连续签到9天即可获得法国state no9邦九号手霜一组\r\n连续签到21天即可半价购买原价186的\r\n安耐晒小金瓶一支'

        else:

            date = datetime.datetime.strptime(str(si.SignInTime), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

            # 判断是否在今天
            now = datetime.datetime.now().strftime('%Y-%m-%d')
            # stf = (now - date).seconds
            if now == date:
                strd = '小可爱今天已经签到过啦，请明天再来~'
            else:

                si.SignInDays += 1
                si.SignInTime = getCurrentDate()
                db.session.add(si)
                db.session.commit()

                strd = '恭喜小可爱签到成功~\r\n您已连续签到{0}天了！\r\n连续签到9天即可获得法国state no9邦九号手霜一组\r\n连续签到21天即可半价购买原价186的\r\n安耐晒小金瓶一支'.format(si.SignInDays)

        FollowerSevice.send_msg(strd, fl_info.OpenId)




