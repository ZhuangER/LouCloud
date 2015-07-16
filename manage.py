# -*- coding: utf-8 -*-

from flask.ext.script import Manager

from loucloud import create_app

app = create_app()
manager = Manager(app)


@manager.command
def run():
    """Run in local machine."""

    app.run(host='0.0.0.0', port=80)


if __name__ == "__main__":
    manager.run()
