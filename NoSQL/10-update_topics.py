#!/usr/bin/env python3
"""this is doc"""


def update_topics(mongo_collection, name, topics):
    """this is doc"""
    mongo_collection.update_many({"name": name}, {"$set:" {"topics": topics}})
