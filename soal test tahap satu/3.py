x = input()


def validate(codes):
    allsym = ['}', '>', ']','{', '<', '[']

    symbol = {
        '[' : ']',
        '{' : '}',
        '<' : '>'
    }

    cls_symbl = ['}', '>', ']']
    opn_symbl = ['{', '<', '[']

    opening = []
    closing = []

    for i in range(len(codes)):
        if codes[i] not in allsym:
            return "FALSE 1"
        if codes[i] not in cls_symbl:
            for j in range(1, len(codes)-i):
                j = len(codes) - (len(codes) + j)
                if symbol[codes[i]] == codes[j]:
                    j = j + len(codes)
                    if j not in closing and i not in opening:
                        opening.append(i)
                        closing.append(j)
                        print(i, " == ", j)
                        break

    if (len(opening) + len(closing)) != len(codes):
        print(len(opening) + len(closing))
        print(len(codes))
        return "FALSE 2 3"

    for i in range(len(opening)):
        opg = opening[i]
        clg = closing[i]
        for j in range(len(closing)):
            if i != j and i == 0:
                if clg - opg > 0:
                    opg_d = opening[j]
                    clg_d = closing[j]
                    if opg < opg_d and clg > clg_d:
                        pass
                    else:
                        return "FALSE 4"
    
    return "TRUE"

print(validate(x))