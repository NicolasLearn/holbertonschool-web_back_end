#!/usr/bin/env python3
""" This module defines the function 'school_by_topic()' """


def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having a specific topic.

    Args:
        mongo_collection (pymongo): Pymongo collection object.
        topics (list[str]): List of topics approached in the school.

    Returns:
        list: All object that contain the topics.
    """
    return list(mongo_collection.find({"topics": topic}))
