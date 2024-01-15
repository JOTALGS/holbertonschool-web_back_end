#!/usr/bin/env python3
"""
   inserts a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """ iasdsdasdsedsaasd dsa. """
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id