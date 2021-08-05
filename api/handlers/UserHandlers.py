#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from datetime import datetime

from flask import g, request, jsonify, current_app, render_template
from flask_restful import Resource
from api.conf.utils import get_mail, get_bcrypt, send_mail

import api.error.errors as error
from api.conf.auth import auth, refresh_jwt
from api.models.models import User
from api.roles import role_required
from api.schemas.schemas import UserSchema

from flask_mail import Message



class Index(Resource):
    @staticmethod
    def get():
        return jsonify({"message": "We're up!"})


class Register(Resource):
    @staticmethod
    def post():

        try:
            # Get password and email.
            email, password = (
                request.json.get("email").strip(),
                request.json.get("password").strip()
            )

        except Exception as why:

            # Log input strip or etc. errors.
            logging.info("email is wrong or email/password not provided. " + str(why))

            # Return invalid input error.
            return error.INVALID_INPUT_422
    

        # Check if any field is none.
        if email is None:
            return error.INVALID_INPUT_422

        # Get user if it is existed.
        user = User.objects(email=email).first()

        # Check if user is existed.
        if user is not None:
            return error.ALREADY_EXIST

        print('low')

        # Create a new user.
        user = User(email=email, password=get_bcrypt().generate_password_hash(password))
        
        user.save()
        
        # Send a verification email
        msg = Message('Kbapp registration verification', sender='n.nomaly@gmail.com', recipients=[email])
        msg.html = render_template('verify_email.html')
        send_mail(msg)

        # Return success if registration is completed.
        return {"status": "registration completed."}


class Login(Resource):
    @staticmethod
    def post():

        try:
            # Get user email and password.
            email, password = (
                    request.json.get("email").strip(),
                    request.json.get("password").strip()
                    )
        except Exception as why:

            # Log input strip or etc. errors.
            logging.info("Email or password is wrong. " + str(why))

            # Return invalid input error.
            return error.INVALID_INPUT_422

        # Check if user information is none.
        if email is None or password is None:
            return error.INVALID_INPUT_422

        # Get user if it is existed.
        user = User.objects(email=email).first()

        if user is None or not get_bcrypt().check_password_hash(user.password, password):
            return error.UNAUTHORIZED
    
        # Check if already logged in
        if user.refresh_token is not None:
            return error.ALREADY_LOGIN;

        # Generate access token.
        access_token = user.generate_auth_token()

        # Generate refresh token.
        refresh_token = refresh_jwt.dumps({"email": email})

        # save the refresh token inside of user document
        user.update(refresh_token=refresh_token.decode())

        # Return access token and refresh token.
        return {
            "access_token": access_token.decode(),
            "refresh_token": refresh_token.decode(),
        }


class Logout(Resource):
    @staticmethod
    @auth.login_required
    def post():

        # Get refresh token.
        refresh_token = request.json.get("refresh_token")

        # Get if the refresh token is in blacklist
        user = User.objects(refresh_token=refresh_token).first()

        # Check refresh token is existed.
        if user is None:
            return {"status": "already invalidated", "refresh_token": refresh_token}

        
        # remove refresh token of the user
        user.update(refresh_token=None)

        # Return status of refresh token.
        return {"status": "invalidated", "refresh_token": refresh_token}


class RefreshToken(Resource):
    @staticmethod
    def post():

        # Get refresh token.
        refresh_token = request.json.get("refresh_token")

        # Get if the refresh token is in blacklist.
        user = User.objects(refresh_token=refresh_token).first()

        # Check refresh token is existed.
        if user is None:

            # Return invalidated token.
            return {"status": "refresh token is invalidated"}

        try:
            # Generate new token.
            data = refresh_jwt.loads(refresh_token)

        except Exception as why:
            # Log the error.
            logging.error(why)

            # If it does not generated return false.
            return False

        # Create user not to add db. For generating token.
        user = User(email=data["email"])

        # New token generate.
        token = user.generate_auth_token()

        # Return new access token.
        return {"access_token": token.decode()}


class ResetPassword(Resource):
    @auth.login_required
    def post(self):

        # Get old and new passwords.
        old_pass, new_pass = request.json.get("old_pass"), request.json.get("new_pass")

        # Get user. g.user generates email address cause we put email address to g.user in models.py.
        user = User.objects(email=g.user).first()

        # Check if user password does not match with old password.
        if user.password != old_pass:

            # Return does not match status.
            return {"status": "old password does not match."}

        # Update password.
        user.update(password=get_bcrypt().generate_password_hash(new_pass))

        # Return success status.
        return {"status": "password changed."}


