#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from flask import Flask

from api.conf.routes import generate_routes
from api.database.database import create_db, db



def create_app():

    # Create a flask app.
    app = Flask(__name__)

    # Set debug true for catching the errors.
    app.config['DEBUG'] = True

    # Mongodb config
    
    app.config['MONGODB_SETTINGS'] = {
            'db': 'User',
            'host': 'localhost',
            'port': 27017
    }

    # Generate routes.
    generate_routes(app)

    # Create mongo database
    create_db(app)

    # Return app.
    return app


app = create_app()


