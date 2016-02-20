#!/usr/bin/env python
# encoding: utf-8

# from flask_wtf import Form
# from wtforms import TextField, SubmitField, IntegerField, SelectField
# from .constants import HOST_STATUS, HOST_OK
# from wtforms.validators import Required, AnyOf

# class AddHostForm(Form):
#     name = TextField(u'Hostname', [Required()])
#     username = TextField(u'Username', [Required()])
#     password = TextField(u'Password', [Required()])
#     status_code = SelectField(
#         u'StatusCode',
#         [AnyOf([str(val) for val in HOST_STATUS.keys()])],
#         choices=[(str(val), label) for val, label in HOST_STATUS.items()],
#         default=HOST_OK)

#     submit = SubmitField(u'Add')
