#!/usr/bin/env python3
""" Module of API views for the API authentication. """
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication."""
   

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth method to determine if the path is protected."""
        return False
    

    def authorization_header(self, request=None) -> str:
        """Authorization header method to get the auth header from the request."""
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """Current user method to get the current user from the request."""
        return None
