class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix
        self._invalid_value = -1

    @property
    def rows(self):
        return len(self._matrix)

    @property
    def cols(self):
        if self.rows == 0:
            return 0
        return len(self._matrix[0])

    @property
    def mat(self):
        return self._matrix

    def __str__(self):
        return str(self._matrix)

    def count_rectangles(self):
        """
        Counts number of rectangles of kumite.

        Returns: list of found rectangles, sorted w.r.t. area
        """

        # prefer cols > rows
        # prefer larger > smaller
        rectangles = [
            (2,8), # 16
            (2,6), # 12
            (4,4), # 16
            (3,4), # 12
            (4,3), # 12
            (2,3), # 6
            (8,2), # 16
            (6,2), # 12
            (3,2), # 6
            (2,2)  # 4
        ]

        return Matrix.count(self.find_rectangles(rectangles))

    def find_rectangles(self, rectangles):
        """searches for rectangles in the given order

        - rectangles - list of tuples, each describing a rectangle (sub-matrix)

        Returns: dictionary with found rectangles

        Example:

          found_rectangles = mat.find_rectangles([(2,2), (2,3)])

        """
        found = { p : 0 for p in rectangles }

        for r in range(self.rows):
            for c in range(self.cols):
                for p in rectangles:
                    if self.test_rectangle_at((r,c), p):
                        found[p] += 1
                        self.invalidate((r,c), p)

        return found

    def test_rectangle_at(self, (r,c), (height,width)):
        """
        searches for a rectangle at position (r,c) with dimensions (height,width)
        """
        if height == 0 or width == 0:
            return True

        if r + height > self.rows:
            return False
        if c + width > self.cols:
            return False

        # value at (r,c)
        num = self._matrix[r][c]

        # check whether (r,c) is is valid
        if num == self._invalid_value:
            return False

        # check rows/cols for having the same `num'
        for i in range(height):
            for k in range(width):
                if self._matrix[r + i][c + k] != num:
                    return False

        return True

    def invalidate(self, (r,c), (height,width)):
        """
        invalidate a rectangle at coordinates (r,c) with dimension (height,width)
        """
        for i in range(height):
            for k in range(width):
                if r + i < self.rows and c + k < self.cols:
                    self._matrix[r + i][c + k] = self._invalid_value

    @staticmethod
    def count(rectangles_dict):
        """count number of rectangles
        Returns: number of rectangles, sorted w.r.t. area
        """
        num = { (r*c):0 for (r,c),val in rectangles_dict.items() }

        # do counting
        for p, val in rectangles_dict.items():
            num[p[0]*p[1]] += val

        # convert dictionary to list of tuples
        num = [(s,v) for s,v in num.items()]

        # sort tuples w.r.t. area (first entry)
        num.sort(key = lambda x: x[0])

        # omit area
        num = [v for (s,v) in num]

        return num
