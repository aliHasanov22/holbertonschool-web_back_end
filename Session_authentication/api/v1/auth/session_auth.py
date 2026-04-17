#!/usr/bin/env python3
""" Module of API views for the API authentication. """
import os

from flask import app, jsonify, request
from typing import List, TypeVar
from Session_authentication.api.v1 import auth
from api.v1.auth.auth import Auth
import uuid
import json


class SessionAuth(Auth):
    """SessionAuth class that inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """"Create session id for user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """return user id according to session id"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns current user based on session id from cokie"""
        from models.user import User
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        if user_id is None:
            return None

        return User.get(user_id)

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login route for session auth"""
    from models.user import User
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == "":
        return json.jsonify({"error": "email missing"}), 400

    if password is None or password == "":
        return json.jsonify({"error": "password missing"}), 400

    try:
        Users = User.search({'email': email})
    except Exception:
        Users = []

    if not Users:
        return json.jsonify({"error": "no user found for this email"}), 404

    user = Users[0]
    if not user.is_valid_password(password):
        return json.jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return response
