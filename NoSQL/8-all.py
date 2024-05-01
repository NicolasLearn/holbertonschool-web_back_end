#!/usr/bin/env python3
""" This module defines the function 'list_all()' """


def list_all(mongo_collection):
    """Python function that lists all documents in a collection.
    
    Returns: empty list if no document in the collection.
    """
    return mongo_collection.find()
