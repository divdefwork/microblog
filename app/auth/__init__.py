# -*- coding=utf-8 -*-
# !/usr/bin/env python3


from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes  # !END
