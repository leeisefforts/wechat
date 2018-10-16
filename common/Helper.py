import uuid, requests, json, datetime
import xml.etree.ElementTree as ET
from application import app, db
from common.modals.Account import Account

class WeChatService():
    def dict_to_xml(self, dict_data):
        xml = ["<xml>"]
        for k, v in dict_data.items():
            xml.append("<{0}>{1}</{0}>".format(k, v))
        xml.append("</xml>")

        return "".join(xml)

    def xml_to_dict(self, xml_data):
        xml_dict = {}
        root = ET.fromstring(xml_data)
        for child in root:
            xml_dict[child.tag] = child.text
        return xml_dict

    def get_nonce_str(self):
        '''
        获取随机字符串
        :return:
        '''
        return str(uuid.uuid4()).replace('-', '')

    def getAccessToken(self):

        token = ''
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={0}&secret={1}" \
            .format(app.config['appid'], app.config['appkey'])

        r = requests.get(url=url)
        if r.status_code != 200 or not r.text:
            return token

        data = json.loads(r.text)
        now = datetime.datetime.now()
        date = now + datetime.timedelta(seconds=data['expires_in'] - 200)
        model_token = Account()
        model_token.created_time = self.getCurrentDate()
        model_token.expired_time = date.strftime("%Y-%m-%d %H:%M:%S")
        model_token.created_time = self.getCurrentDate()
        db.session.add(model_token)
        db.session.commit()
        return data['access_token']

    '''
    获取时间
    '''

    def getCurrentDate(format="%Y-%m-%d %H:%M:%S"):
        return datetime.datetime.now().strftime(format)


    '''
    获取格式化的时间
    '''

    def getFormatDate(date=None, format="%Y-%m-%d %H:%M:%S"):
        if date is None:
            date = datetime.datetime.now()

        return date.strftime(format)
