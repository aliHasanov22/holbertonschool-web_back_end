#!/usr/bin/env python3
"""
Module for hashing passwords with bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Return a salted, hashed password as a byte string.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
