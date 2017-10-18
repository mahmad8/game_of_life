"""
Die Hard demonstration run.
Go to http://localhost:8888 after starting.
"""

from game_boards.enums import GameBoards, BoardBoundaries
from web_app.web_application import GameDisplay

GAME_BOARD_HEIGHT = 480
GAME_BOARD_WIDTH = 270

SPEED_MILLISECONDS = 50

BOUNDARY = BoardBoundaries.HARD_BORDERS

# Everything should go extinct at 130 iterations
NUM_ITERATIONS = 130

print('Die Hard demo')
board = GameBoards.DIE_HARD.value(GAME_BOARD_HEIGHT, GAME_BOARD_WIDTH)
GameDisplay(board.board, num_iterations=NUM_ITERATIONS, boundary=BOUNDARY, speed=SPEED_MILLISECONDS)
