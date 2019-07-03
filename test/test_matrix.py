#!/usr/bin/env python2

import unittest
from src import matrix


class TestMatrix(unittest.TestCase):
    def _test_found_rectangles(self, given_matrix, expected_rectangles):
        mat = matrix.Matrix(given_matrix)
        rectangles = mat.count_rectangles()
        self.assertEqual(rectangles, expected_rectangles)

    def test_empty(self):
        mat = matrix.Matrix([])

        self.assertEqual(mat.cols, 0)
        self.assertEqual(mat.rows, 0)

        self.assertEqual(mat.test_rectangle_at((0,0), (0,0)), True)
        self.assertEqual(mat.test_rectangle_at((0,0), (1,1)), False)
        self.assertEqual(mat.test_rectangle_at((1,1), (1,1)), False)

        rectangles = mat.count_rectangles()
        self.assertEqual(rectangles, [0,0,0,0])

    def test_1x4(self):
        mat = matrix.Matrix([[1,1,1,1]])

        self.assertEqual(mat.test_rectangle_at((0,0), ((0,0))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,1))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,2))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,3))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,4))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((2,1))), False)
        self.assertEqual(mat.test_rectangle_at((0,2), ((1,2))), True)

        self.assertEqual(mat.find_rectangles([(1,1)]), {(1,1): 4})

        mat = matrix.Matrix([[1,1,1,1]])
        self.assertEqual(mat.find_rectangles([(1,2)]), {(1,2): 2})

        mat = matrix.Matrix([[1,1,1,1]])
        self.assertEqual(mat.find_rectangles([(1,3)]), {(1,3): 1})

        mat = matrix.Matrix([[1,1,1,1]])
        self.assertEqual(mat.find_rectangles([(1,4)]), {(1,4): 1})

    def test_2x2(self):
        mat = matrix.Matrix([[1,1], [1,1]])

        self.assertEqual(mat.test_rectangle_at((0,0), ((0,0))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,1))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,2))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((2,1))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((2,2))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,3))), False)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,3))), False)

        self.assertEqual(mat.find_rectangles([(1,1)]), {(1,1): 4})

        mat = matrix.Matrix([[1,1], [1,1]])
        self.assertEqual(mat.find_rectangles([(1,2)]), {(1,2): 2})

        mat = matrix.Matrix([[1,1], [1,1]])
        self.assertEqual(mat.find_rectangles([(2,1)]), {(2,1): 2})

        mat = matrix.Matrix([[1,1], [1,1]])
        self.assertEqual(mat.find_rectangles([(2,2)]), {(2,2): 1})


    def test_0100_horizontal(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1]])
        rectangles = mat.find_rectangles([(2,3)])
        self.assertEqual(rectangles, {(2,3): 1})

    def test_0100_vertical(self):
        mat = matrix.Matrix([[1,1],
                             [1,1],
                             [1,1]])
        rectangles = mat.find_rectangles([(3,2)])
        self.assertEqual(rectangles, {(3,2): 1})

    def test_example_0200(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1],
                             [1,1,0],
                             [1,1,0],
                             [1,1,0],
                             [2,2,2]])
        rectangles = mat.find_rectangles([(2,3), (3,2)])
        self.assertEqual(rectangles, {(2,3): 1, (3,2): 1})

    def test_no_overlap_2x2(self):
        mat = matrix.Matrix([[0,1,1],
                             [1,1,1],
                             [1,1,3]])
        rectangles = mat.find_rectangles([(2,2)])
        self.assertEqual(rectangles, {(2,2): 1})

    def test_invalidate_1x1_at_0x0(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1],
                             [1,1,1]])

        mat.invalidate((0,0), (1,1))

        self.assertEqual(mat.mat, [[-1,1,1],
                                   [1,1,1],
                                   [1,1,1]])

    def test_invalidate_2x2_at_0x0(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1],
                             [1,1,1]])

        mat.invalidate((0,0), (2,2))

        self.assertEqual(mat.mat, [[-1,-1,1],
                                   [-1,-1,1],
                                   [1,1,1]])

    def test_invalidate_2x2_at_1x1(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1],
                             [1,1,1]])

        mat.invalidate((1,1), (2,2))

        self.assertEqual(mat.mat, [[1,1,1],
                                   [1,-1,-1],
                                   [1,-1,-1]])


if __name__ == '__main__':
    unittest.main()
