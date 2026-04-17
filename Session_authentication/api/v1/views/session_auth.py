#!/usr/bin/env python3
""" Module of API views for the API authentication. """
import os
from flask import app, jsonify, request
from typing import List, TypeVar
from Session_authentication.api.v1 import auth
import json


@app.route('/auth_session/login', methods=['POST'], strict_slashes=False)
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
