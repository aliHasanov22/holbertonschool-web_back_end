#!/usr/bin/env python3
"""this is documentation for this file"""


def update_topics(mongo_collection, name, topics):
    """this is docmentation sfor this file"""
    mongo_collection.update_many({"name": name}, {"$set:" {"topics": topics}})
