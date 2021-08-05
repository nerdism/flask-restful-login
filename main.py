#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from flask import Flask

from api.conf.routes import generate_routes

from config.config import (MONGO_DB, MONGO_HOST, MONGO_PORT ,
        MAIL_SERVER, MAIL_PORT, MAIL_PASSWORD, MAIL_USE_SSL, MAIL_USERNAME, MAIL_PASSWORD,
        APP_DEBUG)

from api.conf.utils import init_mail, init_bcrypt
from api.database.database import init_db
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


    # Generate routes.
    generate_routes(app)

    init_mail(app)

    init_bcrypt(app)

    init_db(app)

    # Return app.
    return app


app = create_app()
