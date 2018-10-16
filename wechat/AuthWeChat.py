from flask import Blueprint
from application import app, db
from common.modals.Account import Account
import requests, datetime

route_auth = Blueprint('wechat_page', __name__)


@route_auth.route('/authWeChat')
def authWeChat():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}'.format(
        app.config['APPID'], app.config['APPSERCRETID'])
    res = requests.get(url)
    res = res.json()

    account = Account()
    account.AccountName = '美货美铺'
    account.AppId = app.config['APPID']
    account.Created_time = datetime.datetime.now()
    account.Updated_time = datetime.datetime.now()
    account.Access_Token = res['access_token']
    account.Expires_In = res['expires_in']

    db.session.add(account)

    db.session.commit()

    return res['access_token']

@route_auth.route('/{id}')
def index_msg():
    return 'success'
