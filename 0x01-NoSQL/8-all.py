#!/usr/bin/env python3
"""function that lists all documents in a collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """lists all documents in a collection"""
    docs = mongo_collection.find()
    if docs:
        return docs
    return []
