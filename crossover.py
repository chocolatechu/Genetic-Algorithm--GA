import random


#单点交叉
def crossover(encode, CV, Bit):
    #第几个encode
    for i in range(0, len(encode), 2):
        for j in range(len(Bit)):
            r = random.random()
            if r < CV:
                p = random.randint(1, Bit[j]-1)
                encode[i][j][p:], encode[i + 1][j][p:] = encode[i + 1][j][p:], encode[i][j][p:]