#!/usr/bin/env python3
"""Insert a document in Python"""
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs: dict):
    """Write a Python function that inserts a new document in a collection based on kwargs:

        Prototype: def insert_school(mongo_collection, **kwargs):
        mongo_collection will be the pymongo collection object
        Returns the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
