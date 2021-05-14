#!/usr/bin/env python3

from tictactoe import print_board, insert_player_move, winner_outcome, game_status


def test_print_board():
    # test for when the board is empty
    rows = ['   |   |  ', '---+---+---', '   |   |  ', '---+---+---', '   |   |  ']
    board = print_board()
    assert '\n'.join(rows) == board


def test_insert_player_move():
    # need to ensure that there is something in this location in the game board to test this out
    # (or not if testing for True)
    result = insert_player_move(10, 'X')
    assert result == False


def test_winner_outcome():
    winner = 4
    result = winner_outcome()
    assert result == winner


def test_game_status():
    result = game_status(2, 'X')
    assert result == 'continue'


# for the tictactoe.py file for when testing functions
# Board[1] = 'X'
# Board[2] = ' '
# Board[3] = 'X'
# Board[4] = ' '
# Board[5] = 'O'
# Board[6] = 'O'
# Board[7] = 'O'
# Board[8] = 'X'
# Board[9] = 'X'
