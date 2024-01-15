#!/usr/bin/env python3
"""
    PdasdsadasdasdsadsadDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection_nginx = client.logs.nginx
    num_docs = collection_nginx.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    number_methods = {}
    for method in methods:
        number_methods[method] = collection_nginx.count_documents(
            {"method": method})
    status_check = collection_nginx.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{num_docs} logs\nMethods:")
    for method in methods:
        print(f"\tmethod {method}: {number_methods[method]}")
    print(f"{status_check} status check")