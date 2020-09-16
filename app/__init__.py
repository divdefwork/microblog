# -*- coding=utf-8 -*-
# !/usr/bin/env python3

from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app import routes  # END
