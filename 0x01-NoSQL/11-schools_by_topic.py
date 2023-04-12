#!/usr/bin/env python3
"""Where can I learn Python?"""
from pymongo.collection import Collection
from typing import Type


def schools_by_topic(mongo_collection: Type[Collection], topic: str):
    """Write a Python function that returns the list of school having a specific topic:

        Prototype: def schools_by_topic(mongo_collection, topic):
        mongo_collection will be the pymongo collection object
        topic (string) will be topic searched
    """
    return [item for item in mongo_collection.find(
        {"topic": {"$elemMatch": {"eq": topic}}} # type: ignore
    )]
