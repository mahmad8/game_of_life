# Conway's Game of Life Install/Run Instructions

## Overview

The Game of Life application runs Conway's Game of Life. It is written in Python and has a separate
backend that can run on its own from the command line. The web application uses Tornado Web Framework
to display the game in a browser.

When using the standalone Python application or the web application, a seed board should be supplied as
an argument when starting. There are demostration boards created under web_app/demos, which have
pre-seeded boards.

## Requirements

In order to run the application, you will need python 3.6.3, which is available here: [Python 3.6.3](https://www.python.org/downloads/release/python-363/)

The following Python package are required.

* numpy==1.13.3
* pytest==3.2.3
* scipy==0.19.1
* tornado==4.5.2

To install these packages on your machine, cd into the Game of Life directory and run:
	pip install requirements.txt
			or
	pip3 install requirements.txt.

## Run Game from Command Line

The Game of Life application can run with or without a web server. The main application is written
in Python and can be started as follows:

        export PYTHONPATH=<path to Game of Life directory>
        cd <path to Game of Life directory>
        python game/game_of_life.py <board_json> <num_iterations> <boundary>
        
        eg. python game/game_of_life.py sample_input_board.json --num-iterations 50 --boundary TOROID

Run the application with a seed board and optional arguments. The seed board should be a JSON file
with the following format:

    {
      "board" : [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
      ]
    }

A sample input file is included in the Game of Life directory.

The other options are as follows.
   
    * num_iterations - the number of iterations to run
    * boundary - the board boundary type (HARD or TOROID). Because we do not have an infinite board,
      the game runs with either a fixed-size board (HARD) or a board that wraps.


## Run the Web Application

The web server displays the game board. It will only run on your local machine.

1. Set your python path correctly:
    
        export PYTHONPATH=<path to Game of Life directory>

2. Start the web application by providing a seed board and the following optional arguments:

        * num_iterations - the number of iterations to run
        * boundary - the board boundary type (HARD or TOROID). Because we do not have an infinite board,
          the game runs with either a fixed-size board (HARD) or a board that wraps.
        * speed - the time in milliseconds between state changes

    The invocation looks like this:

        python web_app/web_application.py sample_input_board.json --num-iterations 10 --boundary HARD --speed 1000

3. Go to http://localhost:8888 in your web browser. If you need to change the listening port, you can do so
by changing the LISTENING_PORT constant in web_application.py.

## Tests

The "tests" module contains all functional tests, which are divided into basic ruled-based tests
and more complicated motion tests.

To run tests, use py.test. For example,
   
    cd tests
    py.test

A test function is also included in the game_of_life.py module, which has the following signature.

    test_game(seed, num_of_iterations, expected_state)
    
This function will return true if the expected state matches the state of the game after the specified
number of iterations and false otherwise.

## Support

Feel free to contact Munir Ahmad at __mahmad8@gmail.com__ anytime!