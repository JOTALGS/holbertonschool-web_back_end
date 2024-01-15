#!/usr/bin/env python3
"""
    fdfdffsfsd
"""


def schools_by_topic(mongo_collection, topic):
    """sdfgdsgsdd """
    schools = mongo_collection.find({"topics": topic})
    return schools