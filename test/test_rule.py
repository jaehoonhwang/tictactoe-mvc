import unittest

from tictactoe.model.rule import Rule
from tictactoe.model.grid import Grid

class Unittest_Rule(unittest.TestCase):

    def setUp(self):
        self.test_target = 'x'
        self.horizontal_grid = Grid()
        self.rule = Rule(self.horizontal_grid)
        self.vertical_grid = Grid()
        self.diagonal_grid = Grid()
        self.inverse_diag_grid = Grid()

        for y in xrange(self.horizontal_grid.return_col_max()):
            self.horizontal_grid.set_coordinate_value(0, y, self.test_target)

        for x in xrange(self.vertical_grid.return_row_max()):
            self.vertical_grid.set_coordinate_value(x, 0, self.test_target)

        for x in xrange(self.diagonal_grid.return_row_max()):
            self.diagonal_grid.set_coordinate_value(x, x, self.test_target)

        for x in xrange(self.diagonal_grid.return_row_max()):
            self.inverse_diag_grid.set_coordinate_value(x,
                                                self.inverse_diag_grid.return_row_max() - x - 1,
                                                self.test_target)


    def test_horizon_grid(self):
        self.rule.update_grid(self.horizontal_grid)
        self.assertTrue(self.rule._check_horizontal(self.test_target))

    def test_vertical_grid(self):
        self.rule.update_grid(self.vertical_grid)
        self.assertTrue(self.rule._check_vertical(self.test_target))

    def test_diagonal_grid(self):
        self.rule.update_grid(self.diagonal_grid)
        self.assertTrue(self.rule._check_diagonal(self.test_target))

    def test_inverse_diag_grid(self):
        self.rule.update_grid(self.inverse_diag_grid)
        self.assertTrue(self.rule._check_diagonal(self.test_target))

    def test_invalid_horizontal_grid(self):
        self.assertFalse(self._test_horizontal(self.vertical_grid))
        self.assertFalse(self._test_horizontal(self.diagonal_grid))
        self.assertFalse(self._test_horizontal(self.inverse_diag_grid))

    def test_invalid_vertical_grid(self):
        self.assertFalse(self._test_vertical(self.horizontal_grid))
        self.assertFalse(self._test_vertical(self.diagonal_grid))
        self.assertFalse(self._test_vertical(self.inverse_diag_grid))

    def test_invalid_diagonal_grid(self):
        self.assertFalse(self._test_diagonal(self.horizontal_grid))
        self.assertFalse(self._test_diagonal(self.vertical_grid))

    def _test_horizontal(self, grid):
        self.rule.update_grid(grid)
        return self.rule._check_horizontal(self.test_target)

    def _test_vertical(self, grid):
        self.rule.update_grid(grid)
        return self.rule._check_vertical(self.test_target)

    def _test_diagonal(self, grid):
        self.rule.update_grid(grid)
        return self.rule._check_diagonal(self.test_target)
