#!/usr/bin/env python3
"""Define a Python function that inserts a new document
in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    data = {**kwargs}
    result = mongo_collection.insert_one(data)
    return result.inserted_id
