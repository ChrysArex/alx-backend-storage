#!/usr/bin/env python3
"""Define a Python function that changes all topics of a
school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    query_filter = {'name': name}
    update_operation = {'$set': {'topics': topics}}
    result = mongo_collection.update_one(query_filter, update_operation)
