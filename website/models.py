from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Following(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    followings = db.Column(db.String(10000) )
    user_id =  db.Column(db.Integer,db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(100))
    following = db.relationship('Following')
