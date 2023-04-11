#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient

def main():
    collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx

if __name__ == "__main__":
    main()