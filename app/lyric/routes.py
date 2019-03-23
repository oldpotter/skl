# -*- coding: utf-8 -*-
__author__ = 'op'

from app import db
from . import bp
from flask import Response, current_app, request, render_template
import json
from app.models import Lyric


@bp.route('/', methods=['POST', 'GET'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Lyric.query.order_by(Lyric.id.desc()).paginate(page, current_app.config['LYRIC_PER_PAGE'], False)
    return render_template('lyric.html', title=u'歌词', lyrics=pagination.items, pagination=pagination)





@bp.route('/pushlyric', methods=['POST', 'GET'])
def pushLyric():
    '''
    通过微信小程序推送到歌词传到服务器，保存在数据库中
    :return:
    '''

    print (request.data)
    lyric = json.loads(request.data)['lyric']
    lyric = Lyric(artist=lyric['artist'], song=lyric['name'], album=lyric['album'], content=lyric['lyric'])
    db.session.add(lyric)
    db.session.commit()
    res = {}
    return Response(json.dumps(res), mimetype='application/json')


@bp.route('/detail/<id>', methods=['POST', 'GET'])
def detail(id):
    lyric = Lyric.query.get(id)
    items = lyric.content.split('\n')

    return render_template('content.html', items = items)