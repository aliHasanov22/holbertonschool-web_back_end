#!/usr/bin/env python3
""" Module of API views for the API authentication. """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """SessionAuth class that inherits from Auth"""
    pass