# -*- coding: utf-8 -*-
__author__ = 'op'

from . import bp
from flask import render_template

@bp.route('/')
def index():
    return render_template('jianli.html')