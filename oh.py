def crackle_pop(start=1, stop=100):
    output = list(range(start, stop+1))
    for ind, one_num in enumerate(output):
        div_3 = (one_num % 3 == 0)
        div_5 = (one_num % 5 == 0)
        if div_3 and div_5:
            crackle_pop
        elif div_3
            crackle
        elif div_5
            pop

    def cracklepop():
        output = list(range(1, 101))
        for ind, one_num in enumerate(output):
            if one_num % 3 == 0:
                output[ind] = 'Crackle'
            elif one_num % 5 == 0:
                output[ind] = 'Pop'
            if (one_num % 3 == 0) and (one_num % 5 == 0):
                output[ind] = 'CracklePop'
        return output