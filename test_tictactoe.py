#!/usr/bin/env python3

from tictactoe import print_board, insert_player_move, winner_outcome, play_game, main


def test_print_board():
    # test for when the board is empty
    rows = ['   |   |  ', '---+---+---', '   |   |  ', '---+---+---', '   |   |  ']
    board = print_board()
    assert '\n'.join(rows) == board


def test_insert_player_move():
    # need to ensure that there is something in this location in the game board to test this out
    # (or not if testing for True)
    result = insert_player_move(8, 'X')
    assert result == False


def test_winner_outcome():
    winner = 'Player X is the winner!'
    result = winner_outcome()
    assert result == winner


def test_play_game():
    result = play_game(5, 'O')
    assert result == 'That space is already taken. Please pick an empty space.'


def test_main():
    statement = main()
    assert statement == f"To play the game, Players X and O will take turns entering in their moves. Each entry will be" \
                        f" a number 1 through 9.\nThe locations on the board correspond with the numbers as follows:\n" \
                        f" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 \n" \
                        f"The first player to have three of their letter in a row on the board wins the game.\n" \
                        f"Let's play!\n"