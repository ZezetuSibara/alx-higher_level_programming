#!/usr/bin/python3
def safe_print_integer(value):
	"""Prints an integer with "{:d}".format().

    Args:
        value (int): An actual integer to print.

    Returns:
        Should a TypeError or ValueError occurs - False.
        else - True.
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
