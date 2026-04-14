#!/usr/bin/env python3
""" Module of API views for the API authentication. """
import os

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import uuid


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
