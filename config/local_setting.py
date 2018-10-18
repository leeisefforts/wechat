DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bryant:leekobe24@cd-cdb-nmj4h99o.sql.tencentcdb.com:63625/wechat'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ENCODING = "utf8mb4"
SQLALCHEMY_BINDS = {
    'wechat': "mysql+pymysql://bryant:leekobe24@cd-cdb-nmj4h99o.sql.tencentcdb.com:63625/wechat"
}

APPID = 'wx13c3dbe65e5b5b8e'
APPSERCRETID = '5814febca3cf6b2e051175253197ded1'
APPTOKEN = 'meihuomeipu'
EncodingAESKey = 'ydACzeYmdEB6r7uFMg2qfUvvtew7sQjAgav9kOWdgMl'