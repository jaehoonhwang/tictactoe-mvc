from tictactoe.model.grid import Grid


class Rule(object):

    def __init__(self, grid, first_person, second_person):
        self.Grid = grid
        self.Row = len(self.Grid.return_grid())
        self.Col = len(self.Grid.return_grid()[0])
        self.Current_Player = first_person
        self.Next_Player = second_person

    def return_valid_turn(self, turn):
        return self.Current_Player if turn == self.Next_Player else self.Next_Player

    def check_valid_coordinate(self, x, y):
        return self.Grid[x][y] != -1

    def check_win_condition(self, recently_played_move, target):
        r, c = recently_played_move

        return self._check_horizontal(r, target) or self._check_vertical(c, target) or \
            self._check_diagonal(target)

    def set_players(self, first_person, second_person):
        if self.Current_Player and self.Next_Player:
            return
        self.Current_Player = first_person
        self.Next_Player = second_person

    def update_grid(self, grid):
        self.Grid = grid

    def _check_horizontal(self, row, target):
        c_max = self.Col

        for col in xrange(c_max):
            if self.Grid[row][col] != target:
                return False

        return True

    def _check_vertical(self, col, target):
        r_max = self.Row

        for row in xrange(r_max):
            if self.Grid[row][col] != target:
                return False

        return True

    def _check_diagonal(self, target):
        r_max, c_max = self.Row, self.Col

        assert r_max == c_max

        upper_left = True
        upper_right = True

        for i in xrange(r_max):
            if self.Grid[i][i] != target:
                upper_left = False
                break

        for i in xrange(r_max):
            if self.Grid[i][i] != target:
                upper_right = False
                break

        return upper_left or upper_right
