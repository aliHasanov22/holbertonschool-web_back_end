#!/usr/bin/env python3
""" Module of API views for the API authentication. """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth is a class inherited from Auth to
       manage Api authentication"""
   def extract_base64_authorization_header(self, 
         authorization_header: str) -> str:
      """Extract base64 part of auth header for basic auth"""
      if authorization_header is None  or type(authorization_header) != str:
         return None
      if not authorization_header.startswith('Basic '):
         return None
      return authorization_header[6:]
