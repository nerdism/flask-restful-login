#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restful import Api

from api.handlers.UserHandlers import (
    Index,
    Login,
    Logout,
    RefreshToken,
    Register,
    ResetPassword,
    )


def generate_routes(app):

    # Create api.
    api = Api(app)

    # Add all routes resources.
    # Index page.
    api.add_resource(Index, "/")

    # Register page.
    api.add_resource(Register, "/v1/auth/register")

    # Login page.
    api.add_resource(Login, "/v1/auth/login")

    # Logout page.
    api.add_resource(Logout, "/v1/auth/logout")

    # Refresh page.
    api.add_resource(RefreshToken, "/v1/auth/refresh")

    # Password reset page. Not forgot.
    api.add_resource(ResetPassword, "/v1/auth/password_reset")

