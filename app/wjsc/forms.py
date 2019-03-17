# -*- coding: utf-8 -*-
__author__ = 'op'

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length
from app.models import ContactType

class LoginForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')


class ContactForm(FlaskForm):
    title = StringField(u'标题', validators=[DataRequired()], render_kw={ 'placeholder':u'请输入标题'})
    detail = TextAreaField(u'详情', validators=[DataRequired(), Length(min=1, max=5000)], render_kw={'placeholder': u'请输入各场活动信息'})
    type = SelectField(u'类型', choices=[(ContactType.CH, u'书茶会'), (ContactType.DJD, u'读经地')], coerce = int)
    submit = SubmitField(u'提交')




