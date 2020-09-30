# -*- coding=utf-8 -*-
# !/usr/bin/env python3


from flask import Blueprint


bp = Blueprint('main', __name__)

from app.main import routes  # !END
