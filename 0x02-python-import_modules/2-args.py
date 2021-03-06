#!/usr/bin/python3
"""
program that prints the number of and the list of its arguments

Author: Lauren Mugabo Inkingi
"""
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 arguments:")
    else:
        print("{:d} arguments:".format(count))
        for i in range(count):
            print("{:d}: {:s}".format(i + 1, sys.argv[i + 1])
