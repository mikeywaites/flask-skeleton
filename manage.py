#!/usr/bin/python
# -*- coding: utf-8 -*-

import urlparse
import subprocess

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from {{PROJECT_NAME}}.app import create_app
from {{PROJECT_NAME}}.models import db

app = create_app()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def dbshell():

    url = urlparse.urlparse(app.config['SQLALCHEMY_DATABASE_URI'])
    params = {
        'db_name': url.path.strip('/'),
        'user': url.username,
        'host': url.hostname,
    }
    cmd = "psql {db_name} -U {user} -h {host}".format(**params)
    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    manager.run()
