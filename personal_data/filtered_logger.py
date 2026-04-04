#!/usr/bin/env python3
"""
Filtered logger and secure database connection
"""

import logging
import os
import mysql.connector
from typing import Tuple

# ------------------ PII Fields ------------------
PII_FIELDS: Tuple[str, ...] = ("name", "email", "ssn", "password", "phone")


# ------------------ Redacting Formatter ------------------
def filter_datum(fields: Tuple[str, ...], redaction: str, message: str,
                 separator: str) -> str:
    """
    Replace values of specified fields in message with redaction
    """
    for field in fields:
        message = message.replace(f"{field}=", f"{field}={redaction}")
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = ("[HOLBERTON] %(name)s %(levelname)s "
              "%(asctime)-15s: %(message)s")
    SEPARATOR = ";"

    def __init__(self, fields: Tuple[str, ...]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
        )
        return super().format(record)


# ------------------ Logger ------------------
def get_logger() -> logging.Logger:
    """Returns a logger named 'user_data' with RedactingFormatter applied"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
        logger.addHandler(handler)

    return logger


# ------------------ Secure Database Connection ------------------
def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to the MySQL database from environment variables.

    Environment variables:
        PERSONAL_DATA_DB_USERNAME (default: "root")
        PERSONAL_DATA_DB_PASSWORD (default: "")
        PERSONAL_DATA_DB_HOST (default: "localhost")
        PERSONAL_DATA_DB_NAME (required)

    Returns:
        mysql.connector.connection.MySQLConnection: connection object
    """
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    if not database:
        raise ValueError("Env variable PERSONAL_DATA_DB_NAME is not set")

    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )
