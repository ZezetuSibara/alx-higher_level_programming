#!/usr/bin/python3


def safe_print_integer(value):
    """Prints a value with "{:d}".format().

    Args:
        value (int): The value to print.

    Returns:
        Should a TypeError or ValueError occurs - False.
        Else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
