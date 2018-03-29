import random


def mutation(encode, change, Bit):
    for i in range(len(encode)):
        for j in range(len(Bit)):
            for k in range(int(Bit[j])):
                r = random.random()
                if r < change:
                    encode[i][j][k] ^= 1