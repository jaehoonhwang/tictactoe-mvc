from tictactoe.model.player import Player

name_prompt = "Enter your name: "
marker_prompt = "Enter your marker: "

board_prompt = "Enter m, M x M board: "

coord_x_prompt = "Enter x coordinate: "
coord_y_prompt = "Enter y coordinate: "


def ask_player_information():
    name = raw_input(name_prompt)
    marker = raw_input(marker_prompt)
    return Player(name, marker)

def ask_board_size():
    a = input(board_prompt)
    return a

def ask_coordinate():
    x_coord = input(coord_x_prompt)
    y_coord = input(coord_y_prompt)

    return x_coord, y_coord
