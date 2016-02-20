#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Column
from ..extensions import db
from .constants import USER_NORMAL, USER_ADMIN
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(128), nullable=False, unique=True)
    _password = Column('password', db.String(256), nullable=False)
    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)
    # Hide password encryption by exposing password field only.
    password = db.synonym('_password',
                          descriptor=property(_get_password,
                                              _set_password))

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)
        
        
    type_code = Column(db.SmallInteger, default=USER_NORMAL)
    
    def is_admin(self):
        return self.type_code == USER_ADMIN
        
    @classmethod
    def authenticate(cls, login, password):
        user = cls.query.filter(User.name == login).first()

        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False

        return user, authenticated
