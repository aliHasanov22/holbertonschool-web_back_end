#!/usr/bin/env python3
"""this is document this code inserts new dict based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """this is document"""
    result = mongo_collection.insert_many(kwargs)
    return result._id
