i#!/usr/bin/python3
"""
The 101-add_attribute Module
"""


def add_attribute(obj, objname, value):
    """attribute to object is added
    args:
        obj: the class object
        objname: the object name
        value: attribute value
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
