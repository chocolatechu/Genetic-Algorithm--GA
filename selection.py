import copy
import random


def selection(encode, y):
    #计算出每个个体被遗传到下一代群体中的概率；
    s = sum(y)
    pro = [k/s for k in y]
    tmp = []
    #计算出每个个体的累积概率；
    s2 = 0
    for k in pro:
        s2 = s2 + k
        tmp.append(s2)
    #在[0，1]区间内产生一个均匀分布的伪随机数r；
    #若r<q[1]，则选择个体1，否则，选择个体k，使得：q[k-1]<r≤q[k] 成立；
    tmp2 = []
    for j in range(len(encode)):
        r = random.random()
        for i in range(len(tmp)):
            if r <= tmp[i]:
                tmp2.append(i)
                break

    tmp3 = []
    tmp4 = []
    for i in tmp2:
        tmp3.append(copy.deepcopy(encode[i]))
        tmp4.append(y[i])
    encode = tmp3
    y = tmp4