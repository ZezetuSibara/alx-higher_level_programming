#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
  """An integer with "{:d}".format() is printed.

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): An actual integer to print.

    Returns:
        Should a TypeError or ValueError occurs - False.
        Else - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        return False
