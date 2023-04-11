#!/usr/bin/env python3
"""Change school topics"""
from pymongo.collection import Collection
from typing import List


def update_topics(mongo_collection: Collection, name: str, topics: List[str]):
    """Write a Python function that changes all topics of a school document based on the name:

        Prototype: def update_topics(mongo_collection, name, topics):
        mongo_collection will be the pymongo collection object
        name (string) will be the school name to update
        topics (list of strings) will be the list of topics approached in the school"""
    mongo_collection.update_one({"name": name}, {'$set': {'topics': topics}})
