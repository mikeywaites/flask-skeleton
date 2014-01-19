#!/usr/bin/python
# -*- coding: utf-8 -*-

import urlparse
import subprocess

from flask.ext.script import Manager

from {{PROJECT_NAME}} import create_app

manager.add_option('-c', '--config', dest='config', required=False)

app = create_app()

manager = Manager(app)


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
