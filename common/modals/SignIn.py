from application import db, app
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue

class SignIn(db.Model):
    __tablename_ = 'signIn'

    Id = Column(Integer, primary_key =True)
    OpenId = Column(String(128), nullable=False, server_default=FetchedValue())
    SignInTime = Column(DateTime, nullable=False, server_default=FetchedValue())
    SignInDays = Column(Integer, nullable=False, server_default=FetchedValue())