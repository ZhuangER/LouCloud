#!/usr/bin/env python
# encoding: utf-8

from flask_wtf import Form
from wtforms import (TextField, SubmitField, HiddenField, PasswordField)
from wtforms.validators import Required, Length

class LoginForm(Form):
    next = HiddenField()
    login = TextField(u'Username', [Required()])
    password = PasswordField('Password', [Required(), Length(6, 12)])
    submit = SubmitField('Login')
