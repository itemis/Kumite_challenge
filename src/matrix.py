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
