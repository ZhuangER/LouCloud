#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from .config import FlaskConfig
from .extensions import login_manager, db

from .frontend import frontend
from .user import User, user
from .host import host

app = Flask(__name__)
app.config.from_object(FlaskConfig)

# register blueprints
app.register_blueprint(frontend)
app.register_blueprint(host)
app.register_blueprint(user)

# Config SQLAlchemy object
# flask-sqlalchemy
db.init_app(app)

# Update Flask-Login config
login_manager.login_view = 'frontend.login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

login_manager.setup_app(app)


