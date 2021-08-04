#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JsonWebToken

from config.config import JWT_SECRET, JWT_REF_SECRET

# JWT creation. Expires in one hour
jwt = JsonWebToken(JWT_SECRET, expires_in=3600)

# Refresh token creation. Expires in one day (24h)
refresh_jwt = JsonWebToken(JWT_REF_SECRET, expires_in=86400)

# Auth object creation.
auth = HTTPTokenAuth("Bearer")
