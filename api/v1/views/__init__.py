#!/usr/bin/env python3
""" views module
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.login_user import *
from api.v1.views.logout_user import *
from api.v1.views.register_user import *
