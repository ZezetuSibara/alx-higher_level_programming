
#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an value with "{:d}".format().

    Should a ValueError message be caught, a corresponding
    message will be printed to standard error.

    Args:
        value (int): The value to  be printed.

    Returns:
        Should a TypeError or ValueError occurs - False.
        Else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
