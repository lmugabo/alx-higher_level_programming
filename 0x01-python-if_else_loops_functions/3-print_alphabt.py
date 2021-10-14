#!/usr/bin/python3
"""
Print all the letters except q and e
"""
for letter in range(97, 123):
        if letter == 101 or letter == 113:
                continue
        print("{:c}".format(letter), end=''
