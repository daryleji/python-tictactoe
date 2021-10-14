"""
TIC TAC TOE Game using pygame
"""

import pygame
import sys
import numpy as np

# GLOBAL VARIABLES
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
BOARD_ROWS = 3
BOARD_COLUMNS = 3
x_segment = DISPLAY_WIDTH / BOARD_COLUMNS
y_segment = DISPLAY_HEIGHT / BOARD_ROWS
BG_COLOR = (28, 170, 156)
PLAYER_ONE_COLOR = (239, 231, 200)
PLAYER_TWO_COLOR = (66, 66, 66)
# pygame
pygame.init()
window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
# board
board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))


# function for boundary lines
def draw_lines() -> None:
    line_color = (23, 145, 135)
    line_width = 15

    # First horizontal line
    pygame.draw.line(window, line_color, (0, y_segment), (DISPLAY_WIDTH, y_segment), line_width)
    pygame.draw.line(window, line_color, (0, y_segment * 2), (DISPLAY_WIDTH, y_segment * 2), line_width)
    pygame.draw.line(window, line_color, (x_segment, 0), (x_segment, DISPLAY_HEIGHT), line_width)
    pygame.draw.line(window, line_color, (x_segment * 2, 0), (x_segment * 2, DISPLAY_HEIGHT), line_width)


# Initialises a blank board state
def init_board() -> None:
    for col in range(BOARD_COLUMNS):
        for row in range(BOARD_ROWS):
            board[col][row] = 0


# Assigns a player to a square, 0 = empty value, 1 = player 1, 2 = player 2/ai
def mark_square(col: int, row: int, player: int) -> None:
    board[col][row] = player


# Check if the square is empty
def available_square(col: int, row: int) -> bool:
    return board[col][row] == 0


# Check if the board is full
def is_board_full() -> bool:
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row, col] == 0:
                return False
    return True


# Function to draw the figure depending on the player
def draw_figures() -> None:
    CIRCLE_RADIUS = 60
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25

    for col in range(BOARD_ROWS):
        for row in range(BOARD_COLUMNS):
            row_p = int(row * y_segment)
            col_p = int(col * x_segment)
            if board[col][row] == 1:
                pygame.draw.circle(window, PLAYER_ONE_COLOR, (col_p + int(x_segment//2), row_p + int(y_segment//2))
                                   , CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[col][row] == 2:
                pygame.draw.line(window, PLAYER_TWO_COLOR, (col_p + 50, row_p + 50), (col_p + (x_segment-50), row_p + (y_segment-50)), CROSS_WIDTH)
                pygame.draw.line(window, PLAYER_TWO_COLOR, (col_p + (x_segment-50), row_p + 50), (col_p + 50, row_p + (y_segment-50)), CROSS_WIDTH)


# Checking win conditions, made to work with variable grid sizes greater than the standard 3x3
def check_win(player: int) -> bool:
    # Check for vertical completion line
    for col in range(BOARD_COLUMNS):
        if board[col][0] == player and board[col][1] == player and board[col][2] == player:
            draw_vertical_win_line(col, player)
            return True

    # Check for horizontal completion line
    for row in range(BOARD_ROWS):
        if board[0][row] == player and board[1][row] == player and board[2][row] == player:
            draw_horizontal_win_line(row, player)
            return True

    # Check for asc_diagonal completion line
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        draw_asc_diagonal(player)
        return True

    # Check for desc_diagonal completion line
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_vertical_win_line(col: int, player: int) -> None:
    col_p = int(col * x_segment + int(x_segment//2))
    color = (255, 255, 255)
    if player == 1:
        color = PLAYER_ONE_COLOR
    elif player == 2:
        color = PLAYER_TWO_COLOR
    offset = 15
    pygame.draw.line(window, color, (col_p, offset), (col_p, DISPLAY_HEIGHT - offset), 20)


def draw_horizontal_win_line(row: int, player: int) -> None:
    row_p = int(row * y_segment + int(y_segment//2))
    color = (255, 255, 255)
    if player == 1:
        color = PLAYER_ONE_COLOR
    elif player == 2:
        color = PLAYER_TWO_COLOR
    offset = 15
    pygame.draw.line(window, color, (offset, row_p), (DISPLAY_HEIGHT - offset, row_p), 20)


def draw_asc_diagonal(player: int) -> None:
    color = (255, 255, 255)
    if player == 1:
        color = PLAYER_ONE_COLOR
    elif player == 2:
        color = PLAYER_TWO_COLOR
    offset = 15
    pygame.draw.line(window, color, (offset, DISPLAY_HEIGHT - offset), (DISPLAY_WIDTH - offset, offset), 20)


def draw_desc_diagonal(player: int) -> None:
    color = (255, 255, 255)
    if player == 1:
        color = PLAYER_ONE_COLOR
    elif player == 2:
        color = PLAYER_TWO_COLOR
    offset = 15
    pygame.draw.line(window, color, (offset, offset), (DISPLAY_WIDTH - offset, DISPLAY_HEIGHT - offset), 20)


def main():
    player = 1
    window.fill(BG_COLOR)
    draw_lines()
    init_board()
    game_over = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_x_pos = event.pos[0]  # x position
                mouse_y_pos = event.pos[1]  # y position
                # 0, 1, 2 x, y coord version for mouse to grid
                square_row = int(mouse_y_pos // x_segment)
                square_col = int(mouse_x_pos // y_segment)

                if available_square(square_col, square_row):
                    if player == 1:
                        mark_square(square_col, square_row, 1)
                        if check_win(player):
                            game_over = True
                        player = 2
                    elif player == 2:
                        mark_square(square_col, square_row, 2)
                        if check_win(player):
                            game_over = True
                        player = 1

                    draw_figures()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Code to restart and reset the game state, could call main, but would nest many mains within itself
                    # and have nested while loops which don't exit until window is closed
                    player = 1
                    window.fill(BG_COLOR)
                    draw_lines()
                    init_board()
                    game_over = False

        pygame.display.update()


if __name__ == '__main__':
    main()
