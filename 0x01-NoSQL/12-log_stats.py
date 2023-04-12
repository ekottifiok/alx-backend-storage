#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    nginx = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    print("{} logs".format(nginx.count_documents({})))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(
            method,
            len(list(nginx.find({"method": method})))
        ))
    print("{} status check".format(
        len(list(nginx.find({"path": "/status", "method": "GET"})))
    ))
