from application import db , app
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue

class Account(db.Model):
    __tablename_ = 'account'

    Id = Column(Integer, primary_key=True)
    AccountName = Column(String(128), nullable=False, server_default= db.FetchedValue())
    AppId = Column(String(128), nullable=False, server_default= db.FetchedValue())
    Access_Token = Column(String(128), nullable=False, server_default= db.FetchedValue())
    Expires_In = Column(String(128), nullable=False, server_default= db.FetchedValue())
    Created_time = Column(DateTime, nullable=False, server_default= db.FetchedValue())
    Updated_time = Column(DateTime, nullable=False, server_default= db.FetchedValue())