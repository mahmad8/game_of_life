from game_boards.patterns import PATTERNS


class GameBoard:
    """
    An empty Game of Life board.
    """

    def __init__(self, width, height, pattern=None):
        """
        Initialize a game of life board with the specified number of rows and columns and
        an with an optional pattern. If no patternis specified, one can be inserted later
        by calling seed_board.

        :param height: Number of rows in the game board
        :param width: Number of columns in the game board
        :param pattern: Optional 2D array used to the seed the board
        """
        self.num_rows = height
        self.num_cols = width
        self.board = self._create_board(height, width)
        if pattern is not None:
            self.seed_board(pattern)

    def seed_board(self, pattern, offset_rows=None, offset_cols=None):
        """
        Insert the given pattern into the board with the specified row and column offsets,
        defaulting to the center of the board if no offsets are specified.

        :param pattern: 2D array pattern
        :param offset_rows: number of rows to offset the pattern when inserting
        :param offset_cols: numbs of columns to offset the pattern when inserting
        """

        if offset_rows is None:
            offset_rows = self.num_rows // 2
        if offset_cols is None:
            offset_cols = self.num_cols // 2

        if offset_rows + len(pattern) > len(self.board) or offset_cols + len(pattern[0]) > len(self.board[0]):
            raise ValueError("The board with offset is not large enough to fit the seed.")

        for i in range(len(pattern)):
            for j in range(len(pattern[i])):
                self.board[offset_rows + i][offset_cols + j] = pattern[i][j]

    @staticmethod
    def _create_board(num_rows, num_cols):
        """
        Generate a blank game board.

        :param num_rows: number of rows in board
        :param num_cols: number of columns in board
        :return: 2D array game board initialized with zeros.
        """
        array = list()
        for i in range(num_rows):
            array.append([0] * num_cols)
        return array


class RPentomimo(GameBoard):
    """
    R-Pentomimo Game of Life Pattern
    See https://en.wikipedia.org/wiki/File:Game_of_life_fpento.svg
    """

    def __init__(self, rows, cols):
        super().__init__(rows, cols, pattern=PATTERNS['r_pentomimo'])


class Blinker(GameBoard):
    """
    Blinker Game of Life Pattern
    See https://en.wikipedia.org/wiki/File:Game_of_life_blinker.gif
    """

    def __init__(self, rows, cols):
        super().__init__(rows, cols, pattern=PATTERNS['blinker'])


class Acorn(GameBoard):
    """
    Acorn Game of Life Pattern
    See https://en.wikipedia.org/wiki/File:Game_of_life_acorn.svg
    """

    def __init__(self, rows, cols):
        super().__init__(rows, cols, pattern=PATTERNS['acorn'])


class DieHard(GameBoard):
    """
    Diehard pattern.
    See https://en.wikipedia.org/wiki/File:Game_of_life_diehard.svg
    """

    def __init__(self, rows, cols):
        super().__init__(rows, cols, pattern=PATTERNS['die_hard'])


class InfiniteBlockTrail(GameBoard):
    """
    Infinite growth pattern.
    See https://en.wikipedia.org/wiki/File:Game_of_life_infinite2.svg
    """

    def __init__(self, rows, cols):
        super().__init__(rows, cols, pattern=PATTERNS['infinite_block_trail'])
