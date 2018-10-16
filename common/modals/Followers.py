from application import db, app
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue

class Follower(db.Model):
    __tablename__ = 'followers'

    Id = db.column(db.Integer, primary_key=True)
    NickName = db.column(db.String(128), nullable=False, server_default=db.FetchedValue())
    OpenId = db.column(db.String(128), nullable=False, server_default=db.FetchedValue())
    Language = db.column(db.String(128), nullable=False, server_default=db.FetchedValue())
    Sex = db.column(db.Integer, nullable=False, server_default=db.FetchedValue())
    HeadImgUrl = db.column(db.String(256), nullable=False, server_default=db.FetchedValue())
    UpdateTime = db.column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    CreateTime = db.column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    Subscribe_time = db.column(db.DateTime, nullable=False, server_default=db.FetchedValue())
