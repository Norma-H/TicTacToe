#!/usr/bin/env python3

Board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
explanation_statement = f"To play the game, Players X and O will take turns entering in their moves. Each entry will " \
                        f"be a number 1 through 9.\nThe locations on the board correspond with the numbers as follows:\n" \
                        f" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 \n" \
                        f"The first player to have three of their letter in a row on the board wins the game.\n" \
                        f"Let's play!\n"

def print_board():
    rows = []
    rows.append(f' {Board[1]} | {Board[2]} | {Board[3]}')
    rows.append('---+---+---')
    rows.append(f' {Board[4]} | {Board[5]} | {Board[6]}')
    rows.append('---+---+---')
    rows.append(f' {Board[7]} | {Board[8]} | {Board[9]}')
    return '\n'.join(rows)


def insert_player_move(location, player):
    if Board[location] == ' ':
        Board[location] = player
        return True
    else:
        return False


def winner_outcome():
    options = [[Board[1], Board[2], Board[3]], [Board[4], Board[5], Board[6]], [Board[7], Board[8], Board[9]],
               [Board[1], Board[5], Board[9]], [Board[2], Board[5], Board[8]], [Board[3], Board[5], Board[6]]]
    for one_set in options:
        if 'X' == one_set[0] and 'X' == one_set[1] and 'X' == one_set[2]:
            return 'Player X is the winner!'
        elif 'O' == one_set[0] and 'O' == one_set[1] and 'O' == one_set[2]:
            return 'Player O is the winner!'
    else:
        for one_set in options:
            if ' ' == one_set[0] or ' ' == one_set[1] or ' ' == one_set[2]:
                return False  # the game is not over
        else:
            return 'It is a tie!'


def play_game(location, player):
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
                    print('That space is already taken. Please pick an empty space.')
                    player_input = int(input(f'Player {one_player}, what is your move? '))
                    status = play_game(player_input, one_player)
                continue
            elif type(status) == str:
                print(status)
                playing = False
                break
            elif not status:
                continue


if __name__ == '__main__':
    main()

