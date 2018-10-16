from application import app, db
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue
class ConversationLog(db.Model):
    __tablename__ = 'conversationLog'

    Id = db.column(db.Integer, primary_key = True)
    FromUserName = db.column(db.String(128), nullable=False, server_default=db.FetchedValue())
    ToUserName = db.column(db.String(128), nullable=False, server_default=db.FetchedValue())
    Content = db.column(db.String(128), nullable=False, server_default=db.FetchedValue())
    CreateTime = db.column(db.DateTime, nullable=False, server_default=db.FetchedValue())