# -*- coding: utf-8 -*-
__author__ = 'op'

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')


class ContactForm(FlaskForm):
    city = StringField(u'城市', validators=[DataRequired()])
    detail = TextAreaField(u'详情', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField(u'提交')



