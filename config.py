# -*- coding=utf-8 -*-
# !/usr/bin/env python3

import os


class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
