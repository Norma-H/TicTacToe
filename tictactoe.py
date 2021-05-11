#!/usr/bin/env python3

# 1. create board: dictionary, keys = numbers 1-9, values = will be X or O
# 2. verify user input function: that takes in a number and X/O and puts it in accordingly into the dictionary board
# 3. game function: asks for the user input and calls the verify function and to add the input to the dictionary
# 4. winner check function: checks the board to see if there is 3 in a row / a winner or a tie (or game continues)
# 5. print board function: will print the board with the current positions of the X and Os on the board
# 6. game function will call the winner function and will print out the game outcome. and call the print board function
# 7. put all the game code into the main function and call main

Board = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

def print_board():
    rows = []
    rows.append(f'{Board[1]}   |  {Board[2]} | {Board[3]}')
    rows.append('---+---+---')
    rows.append(f'{Board[4]}   |  {Board[5]} | {Board[6]}')
    rows.append('---+---+---')
    rows.append(f'{Board[7]}   |  {Board[8]} | {Board[9]}')
    return '\n'.join(rows)


def insert_player_move(location, player):
    if Board[location] == '':
        Board[location] = player
        return True
    else:
        return False



# print(print_board())