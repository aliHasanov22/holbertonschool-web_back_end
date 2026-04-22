#!/usr/bin/env python3
"""DB module for the user authentication service"""
from db import DB
from user import User
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """hashed password"""
    return hashpw(password.encode(), gensalt())


class Auth:
    """Auth class to interact with auth data"""

    def __init__(self):
        """initialize auth class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user to the database"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Check whether the provided credentials are valid."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return checkpw(password.encode("utf-8"), user.hashed_password)

    def _generate_uuid(self) -> str:
        """generate uuid"""
        import uuid
        return str(uuid.uuid4())
