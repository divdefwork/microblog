# -*- coding=utf-8 -*-
# !/usr/bin/env python3


from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers  # !END
