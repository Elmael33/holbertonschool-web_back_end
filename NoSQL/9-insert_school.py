#!/usr/bin/env python3
"""Function to insert a new document in a MongoDB collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a MongoDB collection"""
    if mongo_collection is None:
        return []

    documents = mongo_collection.insert_one(kwargs)

    return documents.inserted_id
