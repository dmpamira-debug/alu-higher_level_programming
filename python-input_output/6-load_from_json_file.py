#!/usr/bin/python3
"""Module that defines a load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file

    Args:
        filename (str): name of the JSON file to read

    Returns:
        object: Python data structure represented by the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
