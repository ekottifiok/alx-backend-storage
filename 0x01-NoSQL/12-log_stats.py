#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient

def main():
    """
    Write a Python script that provides some stats about Nginx logs stored in MongoDB:

    Database: logs
    Collection: nginx
    Display (same as the example):
    first line: x logs where x is the number of documents in this collection
    second line: Methods:
    5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
    one line with the number of documents with:
    method=GET
    path=/status
    You can use this dump as data sample: dump.zip

    The output of your script must be exactly the same as the example
    """
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


if __name__ == "__main__":
    main()
