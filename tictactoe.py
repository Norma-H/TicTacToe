#!/usr/bin/env python3

import random


Board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
explanation_statement = f"To play the game, Players X and O will take turns entering in their moves. Each move will " \
                        f"be a number 1 through 9.\nThe locations on the board correspond with the numbers as follows:\n" \
                        f" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 \n" \
                        f"The first player to have three of their letter in a row on the board wins the game.\n" \
                        f"Let's play!\n"


def print_board():
    """ This function returns the game board with the current player positions in a formatted string."""
    rows = []
    rows.append(f' {Board[1]} | {Board[2]} | {Board[3]}')
    rows.append('---+---+---')
    rows.append(f' {Board[4]} | {Board[5]} | {Board[6]}')
    rows.append('---+---+---')
    rows.append(f' {Board[7]} | {Board[8]} | {Board[9]}')
    return '\n'.join(rows)


def insert_player_move(location, player):
    """ This function takes in the entered location for X/O placement and the player whose placing their piece.
        It checks to see if the location is a number 1 through 9 and if not, it returns False.
        It then checks to see whether the location is already occupied by another X/O.
        If the location is empty, the player's X or O piece is placed there and the function returns True.
        If the location is already filled, the function returns False."""
    if location in range(1, 10):
        if Board[location] == ' ':
            Board[location] = player
            return True
        else:
            return False
    else:
        return False


def winner_outcome():
    """ This function checks to see if there is a winner, a tie, or if the game is still going on.
        It goes through each set of 3 locations that would be a winning combination (listed in the options variable).
        The function returns an integer (1 through 4) corresponding to each of the 4 return options:
        If X or O is found in all three locations of a set, the function returns integer 1 or 2, respectively.
        If there is no winner and at least one empty location, the function returns integer 3, indicating the game isn't over.
        If all the locations are filled and there was no winner, the function returns integer 4, indicating a tie."""
    options = [[Board[1], Board[2], Board[3]], [Board[4], Board[5], Board[6]], [Board[7], Board[8], Board[9]],
               [Board[1], Board[5], Board[9]], [Board[2], Board[5], Board[8]], [Board[3], Board[5], Board[7]],
               [Board[3], Board[6], Board[9]], [Board[1], Board[4], Board[7]]]
    for one_set in options:
        if 'X' == one_set[0] and 'X' == one_set[1] and 'X' == one_set[2]:
            return 1  # X is the winner
        elif 'O' == one_set[0] and 'O' == one_set[1] and 'O' == one_set[2]:
            return 2  # O is the winner
    else:  # if there is no winner
        if ' ' in Board.values():  # still empty spaces
            return 3  # the game is not over
        else:
            return 4  # no empty spaces --> tie game


def game_status(location, player):
    """ This function takes in the entered location for X/O placement and the player whose placing their piece.
        It calls the insert_player_move function and receives a returned value of True or False.
        If the received value is True, it calls the winner_outcome function to check the status of the game.
        This function returns a string. Four of the string values are based on the value from winner_outcome indicating:
        (1) X is the winner, (2) O is the winner, (3) the game continues, or (4) tie game
        If insert_player_move returns False, this function returns a string indicating that the player needs to
        re-enter a location."""
    status = insert_player_move(location, player)
    if status:
        outcome = winner_outcome()
        if outcome == 1:
            return 'Player X is the winner!'
        elif outcome == 2:
            return 'Player O is the winner!'
        elif outcome == 3:
            return 'continue'  # continue playing the game
        elif outcome == 4:
            return 'It is a tie!'
    else:
        return 're-enter'  # player needs to enter a new / empty location


def play_game():
    """ This function is for playing the game.
        It contains a while loop that continues until the game is over and a for loop for alternating player turns.
        It calls the print_board function before each new turn and asks for each player's input.
        It calls the game_status function and based on the return value does one of three options:
        (1) continuously asks the user for valid input if it was invalid, (2) prints the winner/tie statement and ends
        the game, or (3) continues the game if it is not over
        The function returns the outcome of the game."""
    computer_status = None
    while computer_status != 'y' and computer_status != 'n':
        computer_status = input("Would you like to play against a computer? (y/n) ").strip()
        print(computer_status)
    playing = True
    avail_spots = [1,2,3,4,5,6,7,8,9]
    while playing:
        for one_player in ['X', 'O']:  # alternating turns between players
            print(print_board())
            if computer_status == 'y':
                if one_player == 'X':
                    player_input = ''
                    while not player_input.isdigit():  # validate the user input a digit
                        player_input = input(f'Player {one_player}, what is your move? ').strip()
                elif one_player == 'O':
                    player_input = random.choice(avail_spots)
                    print(f'Player {one_player} placed a piece at location {player_input}.')
            elif computer_status == 'n':
                player_input = ''
                while not player_input.isdigit():  # validate the user input a digit
                    player_input = input(f'Player {one_player}, what is your move? ').strip()
            status = game_status(int(player_input), one_player)  # placing the piece, determining game status
            while 're-enter' in status:  # keep asking the player until it is a valid/empty location entry
                print('Please pick a valid and empty space.')
                player_input = int(input(f'Player {one_player}, what is your move? ').strip())
                status = game_status(player_input, one_player)  # once valid, 'status' changes and breaks out of loop
            if 'winner' in status or 'tie' in status:  # the game is over if a string statement was returned
                playing = False  # want to break out of outer loop
                print(print_board())
                game_over = status
                break
            elif 'continue' in status:  # game is not over
                avail_spots.remove(int(player_input))
                continue
    return game_over


def main():
    print(explanation_statement)
    end_outcome = play_game()
    print(end_outcome)


if __name__ == '__main__':
    main()
