def cracklepop():
    output = list(range(1,101))
    for ind, one_num in enumerate(output):
        if one_num%3 == 0:
            output[ind] = 'Crackle'
        elif one_num%5 == 0:
            output[ind] = 'Pop'
        if (one_num%3 == 0) and (one_num%5==0):
            output[ind] = 'CracklePop'
    return output

print(cracklepop())