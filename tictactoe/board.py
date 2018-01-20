from tictactoe.model.grid import Grid
from tictactoe.model.rule import Rule
from tictactoe.model.utils import GameState, GameCondition
from tictactoe.model.exceptions import InvalidRangeError

from tictactoe.controller import command_prompt

from tictactoe.view.terminal_interface import View



class Board(object):

    def __init__(self):
        self.grid = Grid()
        self.rule = Rule(self.grid)
        self.current_game_state = GameState.Pregame
        self.current_win_condition = None
        self.current_player = None
        self.players = []
        self.turn = 0
        self.view = View(self.grid)

        self._initialize()

    def play(self):
        self.current_game_state = GameState.Playing

        while self.current_game_state == GameState.Playing:
            self.view.show_board()
            x, y = command_prompt.ask_coordinate()
            current_marker = self.current_player.marker
            try:
                self.grid.set_coordinate_value(x, y, current_marker)
            except InvalidRangeError:
                self._handle_invalid_range_error()
                continue

            self.turn += 1
            self.rule.update_grid(self.grid)

            if not self._check_end_condition(x, y):
                self.current_player = self.players[0] if self.players[1] == self.current_player \
                    else self.players[1]

        self.view.show_board()

        if self.current_win_condition == GameCondition.Win:
            self._handle_winner()
        else:
            self._handle_draw()

    def _initialize(self):
        self.current_game_state = GameState.Start
        # Setting up Players
        self.players.append(command_prompt.ask_player_information())
        other_player = command_prompt.ask_player_information()

        while other_player == self.players[0]:
            self._handle_marker_error()
            other_player = command_prompt.ask_player_information()

        self.players.append(other_player)

        first_player_index = self._determine_player()
        self.current_player = self.players[first_player_index]
        self.current_game_state = GameState.Start

    def _check_end_condition(self, x, y):
        is_win = self.rule.check_win_condition((x, y), self.current_player.return_marker())
        is_draw = True if self.turn > 8 else False

        if is_win or is_draw:
            self.current_game_state = GameState.End
            self.current_win_condition = GameCondition.Win if is_win else GameCondition.Draw
            return True

        return False

    def _handle_winner(self):
        winner_prompt = "The winner of the game is: {0}".format(str(self.current_player))
        print winner_prompt
        return

    def _handle_draw(self):
        draw_prompt = "The game was draw"
        print draw_prompt
        return

    def _handle_marker_error(self):
        marker_error = "Can't use same marker."
        print marker_error

    def _handle_invalid_range_error(self):
        invalid_range_error = "Can't use those coordinates, out of range"
        print invalid_range_error

    def _determine_player(self):
        import random

        return random.randint(0, 1)
