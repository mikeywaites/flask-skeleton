#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

mod = Blueprint('example', __name__, url_prefix='/example')


@mod.route('')
def home():
    return render_template("example/home.html")
