#!/usr/bin/env python3
""" Module of API views for the API authentication. """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth is a class inherited from Auth to
       manage Api authentication"""
    pass
