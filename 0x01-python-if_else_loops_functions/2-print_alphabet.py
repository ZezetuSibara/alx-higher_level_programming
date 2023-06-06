#!/usr/bin/python3
# 2-print_alphabet.py

"""Compute alphabet in lowercase, no new line to follow."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
