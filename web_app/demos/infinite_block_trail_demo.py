"""
Infinite Block Trail demonstration run.
Go to http://localhost:8888 after starting.
"""

from game_boards.enums import GameBoards, BoardBoundaries
from web_app.web_application import GameDisplay

GAME_BOARD_HEIGHT = 480
GAME_BOARD_WIDTH = 270

SPEED_MILLISECONDS = 25

BOUNDARY = BoardBoundaries.TOROID

# Change the following constant to limit the number of iterations.
NUM_ITERATIONS = None

print('Infinite Block Trail demo')
board = GameBoards.INFINITE_BLOCK_TRAIL.value(GAME_BOARD_HEIGHT, GAME_BOARD_WIDTH)
GameDisplay(board.board, num_iterations=NUM_ITERATIONS, boundary=BOUNDARY, speed=SPEED_MILLISECONDS)
