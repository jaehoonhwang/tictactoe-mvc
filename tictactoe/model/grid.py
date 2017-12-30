from tictactoe.model import space
from tictactoe.model.decorators import range_check

class Grid(object):

    def __init__(self, m=3, n=3):
        self.m = m
        self.n = n
        self.grid = []
        self._initialize_grid()


    def _initialize_grid(self):

        for i in xrange(self.m):
            row = []
            for j in xrange(self.n):
                row.append(space.Space(i, j))

            self.grid.append(row)

    def set_space(self, x, y, value):
        self.grid[x][y].set_value(value)
