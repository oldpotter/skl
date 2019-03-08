# -*- coding: utf-8 -*-
__author__ = 'op'

from . import bp
from flask import render_template


@bp.route('/<string:title>')
def post(title):
    return render_template('sswj.html', title=title)
