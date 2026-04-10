#!/usr/bin/env python3
""" Module of API views for the API authentication. """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract base64 part of Authorization header"""
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode base64 string to utf-8 string"""
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str

        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """operate the user credebtials such as username and password"""
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_cre = decoded_base64_authorization_header.split(':', 1)
        return user_cre[0], user_cre[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        from models.user import User
        try:
            user = User.search({'email': user_email})
            if len(user) == 0:
                return None
            user = user[0]
            if not user.is_valid_password(user_pwd):
                return None
            return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads auth and retrieves the User instance for a request"""
        auth_header = self.authorization_header(request)
        b64AuthHeader = self.extract_base64_authorization_header(auth_header)
        decodedHeader = self.decode_base64_authorization_header(b64AuthHeader)
        user_email, user_pwd = self.extract_user_credentials(decodedHeader)
        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
