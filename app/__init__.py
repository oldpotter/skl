# -*- coding: utf-8 -*-
__author__ = 'op'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()  # bootstrap库
login = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)

    from . import models

    from rili import bp
    app.register_blueprint(bp, url_prefix='/rili')

    from jianli import bp as jianli_bp
    app.register_blueprint(jianli_bp, url_prefix='/jianli')

    from sishuwujing import bp as sswj_bp
    app.register_blueprint(sswj_bp, url_prefix='/sswj')

    from lyric import bp as lyric_bp
    app.register_blueprint(lyric_bp, url_prefix='/lyric')

    from wjsc import bp as wjsc_bp
    app.register_blueprint(wjsc_bp, url_prefix='/wjsc')

    return app

