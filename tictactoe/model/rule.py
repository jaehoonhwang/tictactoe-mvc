from tictactoe.model.grid import Grid


class Rule(object):

    def __init__(self, grid):
        self.Grid = grid
        self.Row = len(self.Grid.return_grid())
        self.Col = len(self.Grid.return_grid()[0])

    def check_win_condition(self, recently_played_move, target):
        r, c = recently_played_move

        return self._check_horizontal(target) or self._check_vertical(target) or \
            self._check_diagonal(target)

    def update_grid(self, grid):
        self.Grid = grid

    def _check_horizontal(self, target):
        check = []

        for row in xrange(self.Row):
            c = []
            for col in xrange(self.Col):
                c.append(self.Grid.return_grid()[row][col].return_value() == target)
            check.append(all(c))

        return any(check)

    def _check_vertical(self, target):
        check = []

        for col in xrange(self.Col):
            c = []
            for row in xrange(self.Row):
                c.append(self.Grid.return_grid()[row][col].return_value() == target)
            check.append(all(c))

        return any(check)

    def _check_diagonal(self, target):
        r_max, c_max = self.Row, self.Col

        if r_max != c_max:
            return False

        upper_left = True
        upper_right = True

        for i in xrange(r_max):
            if self.Grid.return_grid()[i][i].return_value() != target:
                upper_left = False
                break

        for i in xrange(r_max):
            if self.Grid.return_grid()[i][r_max-i-1].return_value() != target:
                upper_right = False
                break

        return upper_left or upper_right
