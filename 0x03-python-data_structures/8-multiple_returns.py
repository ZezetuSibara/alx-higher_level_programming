#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """The length of a string s replaced along with its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
