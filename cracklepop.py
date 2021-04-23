#!/usr/bin/env python3

def cracklepop():
    ''' Creates a list from 1 to 100 inclusive.
        Replaces the numbers that are divisible by 3, 5, or both with the words 'Crackle', 'Pop', or 'CracklePop',
        respectively.
        Returns the edited list with the replaced words. '''
    output = list(range(1,101))
    for ind, one_num in enumerate(output):
        if (one_num % 3 == 0) and (one_num % 5 == 0):
            output[ind] = 'CracklePop'
        elif one_num%3 == 0:
            output[ind] = 'Crackle'
        elif one_num%5 == 0:
            output[ind] = 'Pop'
    return output

print(cracklepop())