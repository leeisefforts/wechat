import uuid, requests, json, datetime
import xml.etree.ElementTree as ET
from application import app, db
from common.modals.Account import Account


def getCurrentDate(format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(format)


def getFormatDate(date=None, format="%Y-%m-%d %H:%M:%S"):
    if date is None:
        date = datetime.datetime.now()

    return date.strftime(format)


def dict_to_xml(dict_data):
    xml = ["<xml>"]
    for k, v in dict_data.items():
        xml.append("<{0}>{1}</{0}>".format(k, v))
    xml.append("</xml>")

    return "".join(xml)


def xml_to_dict(xml_data):
    xml_dict = {}
    root = ET.fromstring(xml_data)
    for child in root:
        xml_dict[child.tag] = child.text
    return xml_dict


class WeChatService():

    @staticmethod
    def get_nonce_str():
        '''
        获取随机字符串
        :return:
        '''
        return str(uuid.uuid4()).replace('-', '')

    @staticmethod
    def getAccessToken():
        token = None

        token_info = Account.query.filter(Account.Expires_In >= getCurrentDate()).first()
        if token_info:
            token = token_info.Access_Token

            return token

        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}" \
            .format(app.config['APPID'], app.config['APPSERCRETID'])

        r = requests.get(url=url)
        if r.status_code != 200 or not r.text:
            return token

        data = json.loads(r.text)
        now = datetime.datetime.now()
        date = now + datetime.timedelta(seconds=data['expires_in'] - 200)

        account = Account()
        account.AccountName = '美货美铺'
        account.AppId = app.config['APPID']
        account.Access_Token = data['access_token']
        account.Created_time = getCurrentDate()
        account.Expires_In = date.strftime("%Y-%m-%d %H:%M:%S")
        account.Updated_time = getCurrentDate()
        db.session.add(account)
        db.session.commit()
        return data['access_token']
