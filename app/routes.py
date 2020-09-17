# -*- coding=utf-8 -*-
# !/usr/bin/env python3


from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app
from app.form import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Іпполіт'},
            'body': 'Яка гидота ця ваша заливна риба !!'
        }
    ]

    return render_template('index.html', title='Головна',
                           user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.queey.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Неправильне ім'я користувача або пароль")
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Увійти', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
