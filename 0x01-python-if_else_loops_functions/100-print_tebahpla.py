#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse, while changing upper- and lower-case."""
ii = 0
for cc in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(cc - ii)), end="")
    ii = 32 if ii == 0 else 0
