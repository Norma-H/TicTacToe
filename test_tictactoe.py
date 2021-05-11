#!/usr/bin/env python3

from tictactoe import print_board


def test_print_board():
    rows = ['   |   | ', '---+---+---', '   |   | ', '---+---+---', '   |   | ']
    board = print_board()
    assert '\n'.join(rows) == board