from tictactoe.model import space
from tictactoe.model.exceptions import InvalidRangeError


class Grid(object):

    def __init__(self, m=3, n=3, init_value=-1):
        self.m = m
        self.n = n
        self.grid = []
        self._initialize_value = init_value
        self._initialize_grid()

    def set_coordinate_value(self, x, y, value):
        if not self._coordinate_check(x, y, value):
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
                row.append(space.Space(i, j, self._initialize_value))

            self.grid.append(row)

    def _coordinate_check(self, x, y, marker):
        if not (self._range_check(x, self.m) and self._range_check(y, self.n)):
            return False
        if self.grid[x][y].return_value() == self._initialize_value:
            return True
        return False

    def _range_check(self, target, target_max, target_min=0):
        if target < target_min or target > target_max - 1:
            return False
        return True
