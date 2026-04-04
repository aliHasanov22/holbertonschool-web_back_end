#!/usr/bin/env python3
"""
Module for handling personal data securely.
"""

import logging
import os
import re
from typing import List
import bcrypt
import mysql.connector
from mysql.connector.connection import MySQLConnection

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Return the log message with specified fields obfuscated.
    """
    pattern = r"({}=)[^{}]*".format("|".join(fields), separator)
    return re.sub(pattern, r"\1" + redaction, message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Return the formatted log record with sensitive fields redacted.
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Return a logger configured for redacting user data.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    if logger.handlers:
        logger.handlers.clear()
    logger.addHandler(handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Return a connection to the MySQL database.
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def main() -> None:
    """
    Read and display rows from the users table with PII redacted.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = cursor.column_names
    logger = get_logger()

    for row in cursor:
        message = "".join(
            "{}={}; ".format(field, value)
            for field, value in zip(fields, row)
        )
        logger.info(message.strip())

    cursor.close()
    db.close()


def hash_password(password: str) -> bytes:
    """
    Return a salted, hashed password as bytes.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Return True if password matches hashed_password, else False.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)


if __name__ == "__main__":
    main()
