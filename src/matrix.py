class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix
        self._sentinel = -1

    @property
    def rows(self):
        return len(self._matrix)

    @property
    def cols(self):
        if self.rows == 0:
            return 0
        return len(self._matrix[0])

    def __str__(self):
        return str(self._matrix)

    def find_rectangles(self):
        return [0,0,0,0]

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
