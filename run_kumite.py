#!/usr/bin/env python2

import numpy as np
import sys
from src import matrix

def main(argv):
    if len(argv) != 2:
        print("Usage: {} <file>".format(argv[0]))
        exit(1)

    try:
        input_file = argv[1]
        file_content = np.genfromtxt(input_file, delimiter=',', dtype=int)
        mat = matrix.Matrix(file_content)
        found_rectangles = mat.count_rectangles()

        print(''.join(map(lambda x: str(x), found_rectangles)))

    except Exception as ex:
        print(ex)
        exit(1)

if __name__ == "__main__":
    main(sys.argv)
