#!/usr/bin/env python3
"""
    sdasdsadsadsade.
"""


def update_topics(mongo_collection, name, topics):
    """
        ChangdsadasdasdasSdaf
    """
    _filter = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(_filter, update)