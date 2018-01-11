from enum import Enum


class GameState(Enum):
    Pregame = 1
    Start = 2
    Playing = 3
    End = 4

class GameCondition(Enum):
    Win = 1
    Draw = 2
