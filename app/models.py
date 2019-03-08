# -*- coding: utf-8 -*-
__author__ = 'op'

from app import db
from datetime import datetime

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