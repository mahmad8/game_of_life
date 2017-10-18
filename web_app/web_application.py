"""
Main web application module. Tornado Web Server is used here. See http://www.tornadoweb.org/en/stable/
"""

import argparse
import json

from tornado import web, ioloop, websocket

from game.game_of_life import GameOfLife
from game_boards.enums import BoardBoundaries

LISTENING_PORT = 8888


class GameDisplay:
    """
    Main class for running the Game of Life web application.
    """

    def __init__(self, board, num_iterations=None, boundary=BoardBoundaries.TOROID, speed=100):
        self.game = GameOfLife(board, num_of_iterations=num_iterations, boundary=boundary)
        self.state_generator = self.game.state_generator()
        self.num_iterations = num_iterations
        self.speed = speed
        self.app = self.register_handlers()
        self._start_server()

    def register_handlers(self):
        app = web.Application([
            (r"/", MainHandler, dict(game=self.game, speed=self.speed)),
            (r"/game_socket", GameSocket, dict(game=self.game, generator=self.state_generator,
                                               num_iterations=self.num_iterations)),
        ])
        return app

    def _start_server(self):
        self.app.listen(LISTENING_PORT)
        print("Server started. Please visit http://localhost:{}".format(LISTENING_PORT))
        ioloop.IOLoop.current().start()


class MainHandler(web.RequestHandler):
    """
    Render the page and populate the game board with the initial state.
    """

    def initialize(self, game, speed):
        """
        Set the game instance in this object.

        :param game: The game instance
        :param speed: Time in milliseconds between state changes
        """

        self.game = game
        self.speed = speed

    def get(self):
        board = self.game.board
        t = {
            'width': len(board[0]),
            'height': len(board),
            'births': self.game.get_live_cell_coordinates(),
            'boundary': self.game.boundary.name,
            'speed': self.speed,
            'port' : LISTENING_PORT,
        }
        self.render("templates/game_template.html", items=t)


class GameSocket(websocket.WebSocketHandler):
    """
    Web socket handler to handle game board state updates.
    """

    def initialize(self, game, generator, num_iterations):
        """
        Set the game state generator in this object.

        :param generator: The game state generator
        """

        self.game = game
        self.generator = generator
        self.num_iterations = num_iterations

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        if message == 'RESET':
            self.game.reset_board()
            self.generator = self.game.state_generator()
        else:
            _, births, deaths, iterations = self.generator.__next__()
            if self.num_iterations and iterations > self.num_iterations:
                self.write_message('STOP')
            else:
                t = {
                    'births': births,
                    'deaths': deaths,
                    'iterations': iterations,
                }
                self.write_message(t)

    def on_close(self):
        print("WebSocket closed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Game of Life')
    parser.add_argument('board_file', type=str, help='Board JSON file')
    parser.add_argument('--num-iterations', type=int, help='Number of iterations to run',
                        required=False, default=None)
    parser.add_argument('--boundary', type=str, help='Boundary type (HARD or TOROID)', required=False,
                        default='HARD')
    parser.add_argument('--speed', type=int, help='Time in milliseconds between state changes.',
                        required=False, default=25)
    args = parser.parse_args()
    with open(args.board_file) as fp:
        board_dict = json.load(fp)
    boundary_type = BoardBoundaries.TOROID if args.boundary == 'TOROID' else BoardBoundaries.HARD_BORDERS
    GameDisplay(board_dict['board'], args.num_iterations, boundary_type, args.speed)
