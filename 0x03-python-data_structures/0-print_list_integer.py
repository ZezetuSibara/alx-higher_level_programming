#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    """All numbers of the list will be printed."""
    for ii in range(len(my_list)):
        print("{:d}".format(my_list[ii]))
