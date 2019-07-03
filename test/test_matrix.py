#!/usr/bin/env python2

import unittest
from src import matrix

class TestDimensions(unittest.TestCase):
    def test_empty(self):
        mat = matrix.Matrix([])
        self.assertEqual(mat.cols, 0)
        self.assertEqual(mat.rows, 0)

    def test_1x1(self):
        mat = matrix.Matrix([[1]])
        self.assertEqual(mat.cols, 1)
        self.assertEqual(mat.rows, 1)

    def test_2x2(self):
        mat = matrix.Matrix([[1,1], [1,1]])
        self.assertEqual(mat.cols, 2)
        self.assertEqual(mat.rows, 2)


class TestRectangleTest(unittest.TestCase):
    def test_empty(self):
        mat = matrix.Matrix([])
        self.assertEqual(mat.test_rectangle_at((0,0), (0,0)), True)
        self.assertEqual(mat.test_rectangle_at((0,0), (1,1)), False)
        self.assertEqual(mat.test_rectangle_at((1,1), (1,1)), False)

    def test_1x4(self):
        mat = matrix.Matrix([[1,1,1,1]])
        self.assertEqual(mat.test_rectangle_at((0,0), ((0,0))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,1))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,2))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,3))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,4))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((2,1))), False)
        self.assertEqual(mat.test_rectangle_at((0,2), ((1,2))), True)

    def test_2x2(self):
        mat = matrix.Matrix([[1,1], [1,1]])
        self.assertEqual(mat.test_rectangle_at((0,0), ((0,0))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,1))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,2))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((2,1))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((2,2))), True)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,3))), False)
        self.assertEqual(mat.test_rectangle_at((0,0), ((1,3))), False)


class TestFindRectangles(unittest.TestCase):
    def test_empty(self):
        mat = matrix.Matrix([])
        rectangles = mat.count_rectangles()
        self.assertEqual(rectangles, [0,0,0,0])

    def test_find_1x1_in_1x4(self):
        mat = matrix.Matrix([[1,1,1,1]])
        self.assertEqual(mat.find_rectangles([(1,1)]), {(1,1): 4})

    def test_find_1x2_in_1x4(self):
        mat = matrix.Matrix([[1,1,1,1]])
        self.assertEqual(mat.find_rectangles([(1,2)]), {(1,2): 2})

    def test_find_1x3_in_1x4(self):
        mat = matrix.Matrix([[1,1,1,1]])
        self.assertEqual(mat.find_rectangles([(1,3)]), {(1,3): 1})

    def test_find_1x4_in_1x4(self):
        mat = matrix.Matrix([[1,1,1,1]])
        self.assertEqual(mat.find_rectangles([(1,4)]), {(1,4): 1})

    def test_find_1x1_in_2x2(self):
        mat = matrix.Matrix([[1,1], [1,1]])
        self.assertEqual(mat.find_rectangles([(1,1)]), {(1,1): 4})

    def test_find_1x2_in_2x2(self):
        mat = matrix.Matrix([[1,1], [1,1]])
        self.assertEqual(mat.find_rectangles([(1,2)]), {(1,2): 2})

    def test_find_2x1_in_2x2(self):
        mat = matrix.Matrix([[1,1], [1,1]])
        self.assertEqual(mat.find_rectangles([(2,1)]), {(2,1): 2})

    def test_find_2x2_in_2x2(self):
        mat = matrix.Matrix([[1,1], [1,1]])
        self.assertEqual(mat.find_rectangles([(2,2)]), {(2,2): 1})


    def test_find_2x3_in_2x3_horizontal(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1]])
        rectangles = mat.find_rectangles([(2,3)])
        self.assertEqual(rectangles, {(2,3): 1})

    def test_find_3x2_in_3x2(self):
        mat = matrix.Matrix([[1,1],
                             [1,1],
                             [1,1]])
        rectangles = mat.find_rectangles([(3,2)])
        self.assertEqual(rectangles, {(3,2): 1})

    def test_find_2x3_and_3x2_in_6x3(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1],
                             [1,1,0],
                             [1,1,0],
                             [1,1,0],
                             [2,2,2]])
        rectangles = mat.find_rectangles([(2,3), (3,2)])
        self.assertEqual(rectangles, {(2,3): 1, (3,2): 1})

    def test_find_1x1_in_3x3(self):
        mat = matrix.Matrix([[0,1,1],
                             [1,1,1],
                             [1,1,3]])
        rectangles = mat.find_rectangles([(2,2)])
        self.assertEqual(rectangles, {(2,2): 1})


class TestInvalidate(unittest.TestCase):
    def test_1x1_at_0x0(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1],
                             [1,1,1]])

        mat.invalidate((0,0), (1,1))

        self.assertEqual(mat.mat, [[-1,1,1],
                                   [1,1,1],
                                   [1,1,1]])

    def test_2x2_at_0x0(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1],
                             [1,1,1]])

        mat.invalidate((0,0), (2,2))

        self.assertEqual(mat.mat, [[-1,-1,1],
                                   [-1,-1,1],
                                   [1,1,1]])

    def test_2x2_at_1x1(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1],
                             [1,1,1]])

        mat.invalidate((1,1), (2,2))

        self.assertEqual(mat.mat, [[1,1,1],
                                   [1,-1,-1],
                                   [1,-1,-1]])


class TestExamples(unittest.TestCase):
    def test_2x3(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1]])
        rectangles = mat.count_rectangles()
        self.assertEqual(rectangles, [0,1,0,0])

    def test_3x2(self):
        mat = matrix.Matrix([[1,1],
                             [1,1],
                             [1,1]])
        rectangles = mat.count_rectangles()
        self.assertEqual(rectangles, [0,1,0,0])

    def test_6x3(self):
        mat = matrix.Matrix([[1,1,1],
                             [1,1,1],
                             [1,1,0],
                             [1,1,0],
                             [1,1,0],
                             [2,2,2]])
        rectangles = mat.count_rectangles()
        self.assertEqual(rectangles, [0,2,0,0])

    def test_no_overlap_2x2(self):
        mat = matrix.Matrix([[0,1,1],
                             [1,1,1],
                             [1,1,3]])
        rectangles = mat.count_rectangles()
        self.assertEqual(rectangles, [1,0,0,0])


if __name__ == '__main__':
    unittest.main()
