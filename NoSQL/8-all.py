#!/usr/bin/env python3
""" Function to list all documents in a collection """


def list_all(mongo_collection):
    if mongo_collection is None:
        return []

    try:
        documents = list(mongo_collection.find())
    except Exception as e:
        print(f"Error occurred while retrieving documents: {e}")
        return []

    return documents
