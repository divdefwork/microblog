# -*- coding=utf-8 -*-
# !/usr/bin/env python3

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
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
