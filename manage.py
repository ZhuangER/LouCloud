#!/usr/bin/env python
# encoding: utf-8

from loucloud import app, db
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from loucloud.user import User, USER_ADMIN, USER_NORMAL

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0'))

@manager.command
def initdb():
    """Init/reset database."""

    db.drop_all()
    db.create_all()

    admin = User(
            name=u'admin',
            password=u'123456',
            type_code=USER_ADMIN)
    demo = User(
            name=u'demo',
            password=u'123456',
            type_code=USER_NORMAL)
    db.session.add(admin)
    db.session.add(demo)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
