#!/usr/bin/python3
"""Module that defines a class_to_json function"""


def class_to_json(obj):
    """Return dictionary description of an object for JSON serialization

    Args:
        obj: instance of a Class

    Returns:
        dict: dictionary representation of the object
    """
    return obj.__dict__
