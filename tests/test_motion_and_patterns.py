"""
Test known patterns.
"""

from game_boards.boards import GameBoard
from game_boards.patterns import PATTERNS
from game.game_of_life import test_game as run_test_game


def test_blinker_makes_perpendicular_pattern_after_one_iteration():
    board = GameBoard(3, 3)
    board.seed_board(PATTERNS['blinker'], 0, 1)
    expected_state = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
    ]
    assert run_test_game(seed=board.board, num_of_iterations=1, expected_state=expected_state) is True


def test_still_life_remains_after_ten_iterations():
    seed = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    expected_state = seed.copy()
    assert run_test_game(seed=seed, num_of_iterations=10, expected_state=expected_state) is True


def test_glider_becomes_still_life_on_fixed_boundary_board():
    seed = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    expected_state = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    assert run_test_game(seed=seed, num_of_iterations=15, expected_state=expected_state) is True
