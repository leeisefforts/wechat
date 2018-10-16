from application import db, app
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue

class SignIn(db.Model):
    __tablename_ = 'signIn'

    Id = db.column(db.Integer, primary_key =True)
    OpenId = db.column(db.String(128), nullable=False, server_default=db.FetchedValue())
    SignInTime = db.column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    SignInDays = db.column(db.Integer, nullable=False, server_default=db.FetchedValue())