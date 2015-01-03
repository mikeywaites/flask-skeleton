#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import path, environ


class Config(object):
    DEBUG = False
    PORT = 5000
    HOST = "0.0.0.0"
    SQLALCHEMY_ECHO = True
    BASE_URL = "http://{{ PROJECT_NAME }}.com"
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    TEMPLATE_FOLDER = path.join(PROJECT_ROOT, 'templates')


def build_db_url(user=None, password=None, addr=None, name=None):
    tmpl = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}"
    return tmpl.format(DB_USER=user or 'postgres',
                       DB_PASS=password or 'root',
                       DB_ADDR=addr or 'localhost',
                       DB_NAME='{{PROJECT_NAME}}')


class DEV(Config):
    DEBUG = True
    SECRET_KEY = "c1893e25-88ec-4ec2-b2fe-4c213413df25"
    SQLALCHEMY_DATABASE_URI = \
        build_db_url(addr=environ.get('DB_PORT_5432_TCP_ADDR'))


class STAGE(Config):
    DEBUG = True


class LIVE(Config):
    SQLALCHEMY_ECHO = False
    DEBUG = True


class TEST(Config):
    SECRET_KEY = "2147d2df-759b-40ac-8013-f6154110a7d0"
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = \
        build_db_url(name='{{PROJECT_NAME}}_test',
                     addr=environ.get('DB_PORT_5432_TCP_ADDR'))
