import sys

with open('data.txt') as f:
    lol = [int(x) for x in f]
lol.sort()
for i in range(len(lol) - 2):
    for k in range(i + 1, len(lol) - 1):
        for j in reversed(range(k, len(lol))):
            if (lol[i] + lol[k] + lol[j]) == 2020:
                print(lol[i] * lol[j] * lol[k])
                sys.exit()
            elif (lol[i] + lol[k] + lol[j]) < 2020:
                break