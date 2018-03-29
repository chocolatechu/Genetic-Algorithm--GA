import random


def population_init(encode, Num, Bit):
    for i in range(Num):
        tmp = []
        for j in Bit:
            tmpVal = []
            for k in range(int(j)):
                tmpVal.append(random.randint(0, 1))
            tmp.append(tmpVal)
        encode.append(tmp)

# 测试
if __name__=="__main__":
    population=[]
    N=200
    V=2
    nbits=(17, 17)
    population_init(population, N, V, nbits)
    print(population)