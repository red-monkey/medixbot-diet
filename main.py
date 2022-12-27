#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from flask import Flask,jsonify
from api.utils.database import db
from api.utils.responses import response_with
from api.utils import responses as resp
from api.routes.food import food_routes
from api.routes.predict import predict_routes
from api.routes.characteristic import characteristic_routes
from api.config.config import DevelopmentConfig,ProductionConfig,TestingConfig
from flask_cors import CORS,cross_origin


def create_app(config):
    app=Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    return app


if os.environ.get('WORK_ENV')=='PROD':
    app_config=ProductionConfig
elif os.environ.get('WORK_ENV')=='TEST':
    app_config=TestingConfig
else:
    app_config=DevelopmentConfig


application=create_app(app_config)
with application.app_context():
    db.create_all()

#Start global http configuration
cors=CORS(application,resources={r"/api/*"})

application.register_blueprint(food_routes,url_prefix='/api/foods')
application.register_blueprint(characteristic_routes,url_prefix='/api/characteristics')
application.register_blueprint(predict_routes,url_prefix='/api/predict')


@application.after_request
def add_header(response):
    return response

@application.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)

@application.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)

@application.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)
