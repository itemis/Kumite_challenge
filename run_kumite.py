#!/usr/bin/env python3

import sys

def main(argv):
    if len(argv) != 2:
        print("Usage: {} <file>".format(argv[0]))
        exit(1)

if __name__ == "__main__":
    main(sys.argv)
