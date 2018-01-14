from tictactoe.model.grid import Grid
from tictactoe.model.rule import Rule
from tictactoe.model.utils import GameState


class View(object):

    def __init__(self, grid):
        self.grid = grid

    def show_board(self):
        board = self.grid.return_grid()
        max_row = len(board)
        max_col = len(board[0])

        for i in xrange(max_row):
            layer = ""
            for j in xrange(max_col):
                layer += "\t" + str(board[i][j].return_value())
            print (layer)

        return
