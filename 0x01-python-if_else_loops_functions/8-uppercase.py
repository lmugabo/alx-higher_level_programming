#!/usr/bin/python3
"""
print uppercase
"""

def uppercase(str):
        for ch in str:
                temp = ch
                if ord(ch) >= 97 and ord(ch) <= 122:
                        temp = chr(ord(ch) - (ord('a') - ord('A')))
                        print("{}".format(temp), end="")
                        print()
