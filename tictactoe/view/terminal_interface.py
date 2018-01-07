from tictactoe.model.grid import Grid
from tictactoe.model.rule import Rule
from tictactoe.model.utils import GameState


class Terminal(object):

    def __init__(self):
        self.Grid = Grid()
        self.Rule = Rule()
        self.Current_State = GameState.Pregame

    
