"""
Acorn demonstration run.
Go to http://localhost:8888 after starting.
"""

from game_boards.enums import GameBoards, BoardBoundaries
from web_app.web_application import GameDisplay

# 400x300 makes a more exciting game that 480x270
GAME_BOARD_HEIGHT = 400
GAME_BOARD_WIDTH = 300

SPEED_MILLISECONDS = 25

BOUNDARY = BoardBoundaries.TOROID

# Change the following constant to limit the number of iterations.
NUM_ITERATIONS = 10


print('Acorn demo')
board = GameBoards.ACORN.value(GAME_BOARD_HEIGHT, GAME_BOARD_WIDTH)
GameDisplay(board.board, num_iterations=NUM_ITERATIONS, boundary=BOUNDARY, speed=SPEED_MILLISECONDS)
