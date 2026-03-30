#!/usr/bin/python3
"""Module that defines a from_json_string function"""
import json


def from_json_string(my_str):
    """Return a Python object represented by a JSON string

    Args:
        my_str (str): JSON string to deserialize

    Returns:
        object: Python data structure represented by the JSON string
    """
    return json.loads(my_str)
