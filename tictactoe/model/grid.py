from tictactoe.model import space
from tictactoe.model.exceptions import InvalidRangeError


class Grid(object):

    def __init__(self, m=3, n=3):
        self.m = m
        self.n = n
        self.grid = []
        self._initialize_grid()

    def set_coordinate_value(self, x, y, value):
        if self._coordinate_check(x, y):
            raise InvalidRangeError
        self.grid[x][y].set_value(value)

    def return_row_max(self):
        return self.m

    def return_col_max(self):
        return self.n

    def return_grid(self):
        return self.grid

    def _initialize_grid(self):
        for i in xrange(self.m):
            row = []
            for j in xrange(self.n):
                row.append(space.Space(i, j))

            self.grid.append(row)

    def _coordinate_check(self, x, y):
        if self._range_check(x, self.m) and self._range_check(y, self.n):
            return True
        else:
            return False

    def _range_check(self, target, target_max, target_min=0):
        if target < target_min and target > target_max:
            return False
        return True
