def isSame(words):
    cocok = []
    for i in range(len(words)):
        if words.count(words[i])>1:
            if len(cocok) == 0:
                cocok.append(words[i])
                print(i+1, end=' ')
            else:
                if words[i] in cocok:
                    print(i+1, end=' ')
    if len(cocok) != []:
        print("false")

n = int(input())
words = []
for i in range(n):
    m = input()
    words.append(m)

isSame(words)