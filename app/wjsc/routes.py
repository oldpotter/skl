# -*- coding: utf-8 -*-
__author__ = 'op'

from app import db
from . import bp
from flask import render_template, redirect, url_for, flash, request
from .forms import LoginForm, ContactForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User, Contact
from werkzeug.urls import url_parse

@bp.route('/', methods=['POST', 'GET'])
@bp.route('/contacts', methods=['POST', 'GET'])
def contacts():
    '''
    联系信息列表
    :return:
    '''
    page = request.args.get('page', 1, type=int)
    pagination = Contact.query.order_by(Contact.id).paginate(page, 10, False)
    return render_template('wjsc/contacts.html', title=u'联系信息', contacts=pagination.items, pagination=pagination)



@bp.route('/add_contact', methods=['GET', 'POST'])
@login_required
def add_contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(title=form.title.data, detail=form.detail.data, type=form.type.data)
        db.session.add(contact)
        db.session.commit()
        flash(u'添加成功')
        return redirect(url_for('wjsc.contacts'))
    return render_template('wjsc/contact.html', title=u'添加信息', form=form)


@bp.route('/edit_contact/<id>', methods=['GET', 'POST'])
def edit_contact(id):
    contact = Contact.query.get(id)
    form = ContactForm(title=contact.title, detail=contact.detail, type=contact.type)
    if form.validate_on_submit():
        contact.title = form.title.data
        contact.detail = form.detail.data
        contact.type = form.type.data
        db.session.commit()
        flash(u'修改成功')
        return redirect(url_for('wjsc.edit_contact', id=id))
    return render_template('wjsc/contact.html', title=u'编辑信息', form=form, id=id)


@bp.route('/detail/<id>', methods=['GET'])
def contact(id):
    contact = Contact.query.get(id)
    return render_template('wjsc/contact_view.html', title=u'信息详情', contact=contact)


@bp.route('/delete_contact/<id>', methods=['GET'])
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash(u'删除成功')
    return redirect(url_for('wjsc.contacts'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # 已经登录
    if current_user.is_authenticated:
        return redirect(url_for('wjsc.contacts'))

    form = LoginForm()
    # 登录操作
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        # 用户名或者密码错误
        if user is None or not user.check_password(form.password.data):
            flash(u'用户名或者密码错误', category='error')
            return redirect(url_for('wjsc.login'))

        login_user(user, remember=form.remember_me)

        # 要跳转的页
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('wjsc.contacts')

        flash(u'欢迎你:{}!'.format(form.username.data))
        return redirect(next_page)

    return render_template('wjsc/login.html', title=u'登录', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('wjsc.contacts'))
