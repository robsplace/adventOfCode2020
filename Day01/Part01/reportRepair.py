import sys

with open('data.txt') as f:
    lol = [int(x) for x in f]
lol.sort()
for i in lol:
    for j in reversed(lol):
        if (i + j) == 2020:
            print(i * j)
            sys.exit()
        elif (i + j) < 2020:
            break