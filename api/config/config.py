#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECURITY_KEY='_5#y2L"F4Q8z\n\xec]/'
    SECURITY_PASSWORD_SALT='passpass'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'production_database.db')
    SQLALCHEMY_ECHO=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'development_database.db')

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'testing_database.db')
