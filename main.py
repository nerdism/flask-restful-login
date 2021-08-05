#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from flask import Flask

from api.conf.routes import generate_routes

from config.config import (MONGO_DB, MONGO_HOST, MONGO_PORT ,
        MAIL_SERVER, MAIL_PORT, MAIL_PASSWORD, MAIL_USE_SSL, MAIL_USERNAME, MAIL_PASSWORD,
        APP_DEBUG, LOG_PATH)

from api.conf.utils import utils
from api.database.database import database
import logging


def create_app():

    
    # Create a flask app.
    app = Flask(__name__)

    # Set debug true for catching the errors.
    app.config['DEBUG'] = APP_DEBUG
    
    # Mongodb config
    
    app.config['MONGODB_SETTINGS'] = {
            'db': MONGO_DB,
            'host': MONGO_HOST,
            'port': MONGO_PORT
    }

    # Mail Config
    app.config['MAIL_SERVER'] = MAIL_SERVER
    app.config['MAIL_PORT'] = MAIL_PORT
    app.config['MAIL_USERNAME'] = MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
    app.config['MAIL_USE_SSL'] = MAIL_USE_SSL

    print(MAIL_SERVER)

    # Log Config
    logging.basicConfig(filename=LOG_PATH, level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

    # Generate routes.
    generate_routes(app)

    with app.app_context():
        utils.init_mail(app)
        utils.init_bcrypt(app)
        database.init_db(app)

    # Return app.
    return app


app = create_app()
