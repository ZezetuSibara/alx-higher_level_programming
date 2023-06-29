#!/usr/bin/python3

def safe_print_division(a, b):
    """The division of a by b is executed."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
