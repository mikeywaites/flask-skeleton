#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_environments import Environments

app = Flask(__name__)
env = Environments(app)
app.config.from_object('{{ PROJECT_NAME }}.config')

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from {{ PROJECT_NAME }}.views import mod as example_mod
app.register_blueprint(example_mod)
