#!/usr/bin/env python3
"""
Module for filtering sensitive data from logs.
"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate the values of the specified fields in a log message.
    """
    pattern = r"({}=)[^{}]*".format("|".join(fields), separator)
    return re.sub(pattern, r"\1" + redaction, message)


class RedactingFormatter(logging.Formatter):
    """
    Formatter that redacts specified fields in log records.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """
        Initialize the formatter with fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Return the formatted log record with sensitive fields redacted.
        """
        return filter_datum(
            self.fields,
            self.REDACTION,
            super(RedactingFormatter, self).format(record),
            self.SEPARATOR
        )
