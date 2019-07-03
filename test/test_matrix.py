#!/usr/bin/env python3

import unittest
from src import matrix


class TestMatrix(unittest.TestCase):
    def _test_found_rectangles(self, given_matrix, expected_rectangles):
        mat = matrix.Matrix(given_matrix)
        rectangles = mat.find_rectangles()
        self.assertEqual(rectangles, expected_rectangles)

    def test_empty(self):
        mat = matrix.Matrix([])

        self.assertEqual(mat.cols, 0)
        self.assertEqual(mat.rows, 0)

        self.assertEqual(mat.test_rectangle_at((0,0), (0,0)), True)
        self.assertEqual(mat.test_rectangle_at((0,0), (1,1)), False)
        self.assertEqual(mat.test_rectangle_at((1,1), (1,1)), False)

        rectangles = mat.find_rectangles()
        self.assertEqual(rectangles, [0,0,0,0])

    def test_1x4(self):
        arr = [[1,1,1,1]]
        mat = matrix.Matrix(arr)

        self.assertEqual(mat.test_rectangle_at((0,0), ((0,0))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,1))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,2))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,3))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,4))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((2,1))), False)

    def test_2x2(self):
        arr = [[1,1],
               [1,1]]
        mat = matrix.Matrix(arr)

        self.assertEqual(mat.test_rectangle_at((0,0), ((0,0))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,1))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,2))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((2,1))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((2,2))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,3))), False)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,3))), False)


if __name__ == '__main__':
    unittest.main()
