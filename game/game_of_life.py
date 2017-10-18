import argparse
import json

import numpy as np
from scipy.signal import convolve2d

from game_boards.enums import BoardBoundaries


class GameOfLife:
    """
    Conway's Game of Life. See https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life.
    """

    def __init__(self, initial_board, num_of_iterations=None, boundary=BoardBoundaries.HARD_BORDERS):
        """
        Initialize the game with a given board

        :param initial_board: 2D array of zeros and ones representing the initial game state
        :param num_of_iterations: Number of iterations to run.
        """
        self.initial_board = initial_board
        self.reset_board()
        self.num_iterations = num_of_iterations
        self.boundary = boundary

    def reset_board(self):
        """
        Sets the game board to the initial state.
        """

        self.board = np.array(self.initial_board)

    def state_generator(self):
        """
        Generator method that tracks the game state.

        :return: Python generator with a tuple of the following elements:
                    1) the game state as a 2D numpy array
                    2) a list of cells that were "born"
                    3) a list of cells that have "died"
                    4) number of iterations completed
        """

        kernel = np.array([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]])
        iteration = 0

        while True:  # (Game of Life does not end)
            # Run 2D convolution with the given kernel to find out how many neighbors each cell has.
            # Boundary option determines whether to run with hard boundaries on the game board or
            # using a toroid board which wraps circularly. These are the two strategies for handling
            # a finite game board. scipy.signal.convolve2d handles these two modes gracefully, which
            # is why it is used here. There is also a performance gain when using numpy/scipy matrix
            # operations as opposed to iterating element-wise over the whole matrix.
            # See https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.signal.convolve2d.html

            # There is a more sophisticated and efficient algorithm for determining next game state
            # (see http://dotat.at/prog/life/life.html) but for clarity and a lack of time, the standard
            # implementation was chosen.

            num_neighbors_board = convolve2d(self.board, kernel, mode='same', boundary=self.boundary.value)

            # Find empty cells that have three neighbors
            birth_coordinates = np.where(np.logical_and(self.board == 0, num_neighbors_board == 3))

            # Find live cells with too few or too many neighbors
            death_coordinates = np.where(
                np.logical_and(
                    self.board == 1,
                    np.logical_or(num_neighbors_board < 2, num_neighbors_board > 3)
                )
            )

            births = np.array(birth_coordinates).transpose().tolist()
            deaths = np.array(death_coordinates).transpose().tolist()
            self.board[birth_coordinates] = 1
            self.board[death_coordinates] = 0

            iteration += 1
            yield self.board, births, deaths, iteration

    def get_live_cell_coordinates(self):
        """
        Return a list of living cells.

        :return: {list} List of cell coordinates (row, col).
        """

        return np.array(np.where(self.board == 1)).transpose().tolist()


def test_game(seed, num_of_iterations, expected_state):
    """
    Test function that returns true if the game state equals an expected state after
    the specified number of iterations have been completed.

    :param seed: 2D array of the initial game board state
    :param num_of_iterations: Number of iterations to run
    :param expected_state: 2D array of the expected state after running the iterations
    :return: True if the game state matches the expected state after the specified number of iterations
             have been completed. False otherwise.
    """

    game = GameOfLife(seed, num_of_iterations=num_of_iterations)
    iteration = 0
    while iteration < num_of_iterations:
        game.state_generator().__next__()
        iteration += 1
    return np.array_equal(game.board, expected_state)


def print_board(board, iteration):
    """
    Print the board state to stdout.

    :param board: 2D array game board
    :param iteration: Iteration number
    """

    print('Iteration: {}'.format('Start' if iteration == 0 else iteration))
    for row in board:
        print(row)
    print()


def run_game_command_line(board, num_iterations, boundary):
    """
    Method that runs the game when invoked from the command line.

    :param board: Input 2d array game board
    :param num_iterations: Number of iterations to run
    :param boundary: {Enum} The boundary type
    """

    game = GameOfLife(board, num_iterations, boundary)
    print("*** Game of Life ***")
    print("Boundary: {}".format(game.boundary))
    print_board(game.board, 0)
    generator = game.state_generator()
    iteration = 0
    while not num_iterations or iteration < num_iterations:
        board, _, _, iteration = generator.__next__()
        print_board(board, iteration)
    print('End of game.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Game of Life')
    parser.add_argument('board_file', type=str, help='board JSON file')
    parser.add_argument('--num-iterations', type=int, help='number of iterations to run',
                        required=False, default=None)
    parser.add_argument('--boundary', type=str, help='boundary type (HARD or TOROID)', required=False,
                        default='HARD')
    args = parser.parse_args()
    with open(args.board_file) as fp:
        board_dict = json.load(fp)
    boundary_type = BoardBoundaries.TOROID if args.boundary == 'TOROID' else BoardBoundaries.HARD_BORDERS
    run_game_command_line(board_dict['board'], args.num_iterations, boundary_type)
