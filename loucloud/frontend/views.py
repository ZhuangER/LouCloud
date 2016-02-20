#!/usr/bin/env python
# encoding: utf-8

from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)
from flask.ext.login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh

from .forms import LoginForm
from ..user import User

frontend = Blueprint('frontend', __name__)

@frontend.route('/', methods=['GET'])
def index():
    return redirect(url_for('user.index'))

@frontend.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('user.index'))

    form = LoginForm(login=request.args.get('login', None),
                     next=request.args.get('next', None))

    if form.validate_on_submit():
        user, authenticated = User.authenticate(form.login.data,
                                    form.password.data)

        if user and authenticated:
            if login_user(user):
                flash("Logged in", 'success')
            return redirect(form.next.data or url_for('user.index'))
        else:
            flash('Sorry, invalid login', 'error')

    return render_template('frontend/login.html', form=form)

@frontend.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out', 'success')
    return redirect(url_for('frontend.index'))
    
