#!/usr/bin/python3
"""Module that defines a to_json_string function"""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object as a string

    Args:
        my_obj: object to serialize to JSON

    Returns:
        str: JSON representation of the object
    """
    return json.dumps(my_obj)
