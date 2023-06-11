#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Delete all characters c and replace with C from a string."""
    copy = [xx for xx in my_string if xx != 'c' and xx != 'C']
    return ("".join(copy))
