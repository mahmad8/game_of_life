"""
Test the basic Game of Life rules.
"""

import pytest
from game.game_of_life import test_game as run_test_game


def test_single_cell_dies_after_one_iteration():
    seed = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],

    ]
    expected_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert run_test_game(seed=seed, num_of_iterations=1, expected_state=expected_state) is True


def test_cell_with_one_neighbor_dies_after_one_iteration():
    seed = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0],

    ]
    expected_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert run_test_game(seed=seed, num_of_iterations=1, expected_state=expected_state) is True


def test_cell_with_two_neighbors_lives_after_one_iteration():
    seed = [
        [1, 0, 0],
        [0, 1, 0],
        [1, 0, 0],

    ]
    expected_state = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    assert run_test_game(seed=seed, num_of_iterations=1, expected_state=expected_state) is True


def test_cell_with_three_neighbors_lives_after_one_iteration():
    seed = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 0],

    ]
    expected_state = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    assert run_test_game(seed=seed, num_of_iterations=1, expected_state=expected_state) is True


@pytest.mark.parametrize("seed, expected_state", [
    ([[1, 1, 1], [1, 1, 0], [0, 0, 0]], [[1, 0, 1], [1, 0, 1], [0, 0, 0]]),
    ([[1, 1, 1], [1, 1, 1], [0, 0, 0]], [[1, 0, 1], [1, 0, 1], [0, 1, 0]]),
    ([[1, 1, 1], [1, 1, 1], [1, 0, 0]], [[1, 0, 1], [0, 0, 1], [1, 0, 0]]),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 0]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]), ])
def test_cell_with_more_than_three_neighbors_dies_after_one_iteration(seed, expected_state):
    """
    Tests with 4, 5, 6, 7, and 8 neighbors.
    """

    assert run_test_game(seed=seed, num_of_iterations=1, expected_state=expected_state) is True


def test_empty_cell_with_three_neighbors_lives_after_one_iteration():
    seed = [
        [0, 0, 1],
        [0, 0, 0],
        [1, 0, 1],

    ]
    expected_state = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    assert run_test_game(seed=seed, num_of_iterations=1, expected_state=expected_state) is True


def test_empty_board_is_empty_after_one_iteration():
    seed = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    expected_state = seed.copy()
    assert run_test_game(seed=seed, num_of_iterations=1, expected_state=expected_state) is True