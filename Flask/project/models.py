from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Album(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    album_name = db.Column(db.String(100), unique=True)
    album_link = db.Column(db.String(100))
    label = db.Column(db.String(100))
    user_id = db.Column(db.Integer)

