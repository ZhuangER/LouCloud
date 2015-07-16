# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import current_app as APP

user = Blueprint('user', __name__, url_prefix='/')

@user.route('/')
def index():
    return "Hello, LouCloud!"
