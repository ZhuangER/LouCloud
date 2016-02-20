#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template, request, redirect, url_for
from flask.ext.login import login_required
from ..decorators import admin_required
from .models import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/', methods=['GET'])
@login_required
def index():
    return render_template("user/index.html")
    
@user.route('/admin', methods=['GET'])
@login_required
@admin_required
def admin():
    users = User.query.filter().all()
    return render_template("user/admin.html", users=users)
