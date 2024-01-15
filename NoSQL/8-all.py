#!/usr/bin/env python3
"""
    lists all documents in a collection.
"""

def list_all(mongo_collection):
    """ asdsdasd asd sad as """
    documents = []
    documents = mongo_collection.find()
    return documents