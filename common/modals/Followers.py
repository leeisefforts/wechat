from application import db, app
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue

class Follower(db.Model):
    __tablename__ = 'followers'

    Id = Column(Integer, primary_key=True)
    NickName = Column(String(128), nullable=False, server_default=FetchedValue())
    OpenId = Column(String(128), nullable=False, server_default=FetchedValue())
    Language = Column(String(128), nullable=False, server_default=FetchedValue())
    Sex = Column(Integer, nullable=False, server_default=FetchedValue())
    HeadImgUrl = Column(String(256), nullable=False, server_default=FetchedValue())
    UpdateTime = Column(DateTime, nullable=False, server_default=FetchedValue())
    CreateTime = Column(DateTime, nullable=False, server_default=FetchedValue())
    Subscribe_time = Column(Integer, nullable=False, server_default=FetchedValue())
