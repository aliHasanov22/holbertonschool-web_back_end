#!/usr/bin/env python3
"""encription intrudaction personal data"""
import re
from typing import List


def filter_datum(fields: list[str], redaction: str, message: str,
                 separator: str) -> str:
    """return the log message obfuscated"""

    return re.sub(f"({'|'.join(fields)})=[^{separator}]*",
                  f"\\1={redaction}", message)
