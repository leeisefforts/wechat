from application import app, db
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue
class ConversationLog(db.Model):
    __tablename__ = 'conversationLog'

    Id = Column(Integer, primary_key = True)
    FromUserName = Column(String(128), nullable=False, server_default=FetchedValue())
    ToUserName = Column(String(128), nullable=False, server_default=FetchedValue())
    Content = Column(String(128), nullable=False, server_default=FetchedValue())
    CreateTime = Column(db.DateTime, nullable=False, server_default=FetchedValue())