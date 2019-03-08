# -*- coding: utf-8 -*-
__author__ = 'op'

from . import bp
from flask import render_template
import requests
from config import Config
from app.models import Rili
from datetime import date
import json
from app import db

'''
{
    "status": 200,//成功状态
    "message": "success",//成功
    "data": {
        "year": 2017,//当前传参公历年
        "month": 5,//当前传参公历月
        "day": 27,//当前传参的公历日
        "lunarYear": 2017,//数字农历年
        "lunarMonth": 5,//数字农历月
        "lunarDay": 2,//数字农历月
        "cnyear": "贰零壹柒 ",//农历中文表示年
        "cnmonth": "五",//农历中文表示月
        "cnday": "初二",//农历中文表示天
        "hyear": "丁酉",//年
        "cyclicalYear": "丁酉",//甲子年
        "cyclicalMonth": "乙巳",//甲子月
        "cyclicalDay": "甲寅",//甲子日
        "suit": "栽种,捕捉,畋猎,馀事勿取",//宜
        "taboo": "开市,动土,祭祀,斋醮,安葬,探病",//禁忌
        "animal": "鸡",//生肖
        "week": "星期六",//星期
        "festivalList": [],//当天节日
        "jieqi": {//当月节气
            "5": "立夏",//5日立夏
            "21": "小满"//21日小满
        },
        "maxDayInMonth": 29,//农历月当前月天数
        "leap": false,//是否是闰月
        "lunarYearString": "丁酉",//是否是大月
        "bigMonth": false//农历年
    }
}
'''

@bp.route('/')
def index():
    today = date.today()
    today_str = today.year + today.month + today.day
    rili = Rili.query.filter_by(date=today_str).first()
    if not rili:
        headers = {'user-agent': 'my-app/0.0.1'}
        result = requests.get(Config.RILI_URL, headers=headers)
        rili_obj = json.loads(result.text)
        if rili_obj['status'] == 200:
            rili = Rili(date=today_str, jsonContent=result.text)
            db.session.add(rili)
            db.session.commit()
    return render_template('rili.html', title=u'日历', rili=json.loads(rili.jsonContent))