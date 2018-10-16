from application import app
from wechat.AuthWeChat import route_auth

app.register_blueprint(route_auth, url_prefix='/wechat')