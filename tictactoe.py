#!/usr/bin/env python3

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
        If X or O is found in all three locations of a set, the function returns a statement indicating the winner.
        If there is no winner and at least one empty location, the function returns False indicating the game isn't over.
        If all the locations are filled and there was no winner, the function returns a statement indicating a tie."""
    options = [[Board[1], Board[2], Board[3]], [Board[4], Board[5], Board[6]], [Board[7], Board[8], Board[9]],
               [Board[1], Board[5], Board[9]], [Board[2], Board[5], Board[8]], [Board[3], Board[5], Board[7]],
               [Board[3], Board[6], Board[9]], [Board[1], Board[4], Board[7]]]
    for one_set in options:
        if 'X' == one_set[0] and 'X' == one_set[1] and 'X' == one_set[2]:
            return 'Player X is the winner!'
        elif 'O' == one_set[0] and 'O' == one_set[1] and 'O' == one_set[2]:
            return 'Player O is the winner!'
    else:
        if ' ' in Board.values():
            return False  # the game is not over
        else:
            return 'It is a tie!'


def play_game(location, player):
    """ This function takes in the entered location for X/O placement and the player whose placing their piece.
        It calls the insert_player_move function and receives a returned value of True or False.
        If the value is True, it calls the winner_outcome function to check the status of the game and if the game
        is over, this function returns the outcome of the game. If winner_outcome returns False, this function returns
        False and the game continues.
        If insert_player_move returns False, this function returns the integer 1, indicating that the player needs to
        re-enter a location"""
    status = insert_player_move(location, player)
    if status:
        outcome = winner_outcome()
        if outcome:
            return outcome  # the game is over
        else:
            return False  # continue playing the game
    else:
        return 1  # player needs to enter a new / empty location


def main():
    print(explanation_statement)
    playing = True
    while playing:
        for one_player in ['X', 'O']:
            print(print_board())
            player_input = int(input(f'Player {one_player}, what is your move? '))
            status = play_game(player_input, one_player)
            if status == 1:
                while status == 1:
                    print('Please pick a valid and empty space.')
                    player_input = int(input(f'Player {one_player}, what is your move? '))
                    status = play_game(player_input, one_player)
                continue
            elif type(status) == str:
                playing = False  # game is over
                print(print_board())
                print(status)
                break
            elif not status:
                continue


if __name__ == '__main__':
    main()

# Board[1] = 'X'
# Board[2] = 'O'
# Board[3] = 'X'
# Board[4] = 'X'
# Board[5] = ' '
# Board[6] = 'O'
# Board[7] = 'O'
# Board[8] = 'O'
# Board[9] = 'X'