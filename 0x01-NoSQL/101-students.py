#!/usr/bin/env python3
"""Top students"""
from pymongo.collection import Collection
from typing import Type
def top_students(mongo_collection: Type[Collection]):
    """Write a Python function that returns all students sorted by average score:

        Prototype: def top_students(mongo_collection):
        mongo_collection will be the pymongo collection object
        The top must be ordered
        The average score must be part of each item returns with key = averageScore
    """
    
    mongo_collection.find({})
    