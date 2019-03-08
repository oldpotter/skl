# -*- coding: utf-8 -*-
__author__ = 'op'

import os
from dotenv import load_dotenv

env_file_path = os.path.join(os.getcwd(), '.env')
load_dotenv(env_file_path)

class Config():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or ('sqlite:///' + os.getcwd() + '/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RILI_URL = 'https://www.sojson.com/open/api/lunar/json.shtml'
    LYRIC_PER_PAGE= 10