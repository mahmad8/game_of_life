from enum import Enum

from game_boards.boards import Acorn, Blinker, RPentomimo, DieHard, InfiniteBlockTrail


class GameBoards(Enum):
    ACORN = Acorn
    BLINKER = Blinker
    R_PENTOMIMO = RPentomimo
    DIE_HARD = DieHard
    INFINITE_BLOCK_TRAIL = InfiniteBlockTrail


class BoardBoundaries(Enum):
    HARD_BORDERS = 'fill'
    TOROID = 'wrap'
