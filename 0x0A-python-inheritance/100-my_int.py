#!/usr/bin/python3
"""
The definition of class MyInt is contained
"""


class MyInt(int):
    """The definition of class MyInt that inherits"""

    def __eq__(self, other):
        """Equals will be overridden, while inverting it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Not-equals will be overridden, while inverting it"""
        return int(self) == int(other)
