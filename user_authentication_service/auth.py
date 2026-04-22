#!/usr/bin/env python3
"""DB module for the user authentication service"""
from db import DB
from user import User
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """hashed password"""
    return hashpw(password.encode(), gensalt())
