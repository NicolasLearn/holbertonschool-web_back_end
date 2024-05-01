#!/usr/bin/env python3
""" This module defines the function 'update_topics()' """


def update_topics(mongo_collection, name, topics):
    """Function that changes all topics of a school document based on the name

    Args:
        mongo_collection (pymongo): Pymongo collection object.
        name (str): School name to be update.
        topics (list[str]): List of topics approached in the school.
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
