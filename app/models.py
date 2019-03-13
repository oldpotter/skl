# -*- coding: utf-8 -*-
__author__ = 'op'

from app import db, login
from datetime import datetime
from werkzeug.security import check_password_hash
from flask_login import UserMixin

class Rili(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(8), unique=True)
    jsonContent = db.Column(db.Text)

class Lyric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(50))
    song =  db.Column(db.String(50))
    album = db.Column(db.String(50))
    content = db.Column(db.Text)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(20), index=True, unique=True)
    detail = db.Column(db.Text)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))