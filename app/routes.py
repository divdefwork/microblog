# -*- coding=utf-8 -*-
# !/usr/bin/env python3

from app import app


@app.route('/')
@app.route('/index')
def index():
	return "Привіт, світ!"
