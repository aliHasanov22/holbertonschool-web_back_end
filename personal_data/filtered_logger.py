#!/usr/bin/env python3
"""encription intrudaction personal data"""
import re
from typing import List


def filter_datum(fields: list[str], redaction: str, message: str,
                 separator: str) -> str:
    """return the log message obfuscated"""

    patt = f"({'|'.join(fields)})=.*?{separator}"
    return re.sub(patt, f"\\1={redaction}{separator}", message)
