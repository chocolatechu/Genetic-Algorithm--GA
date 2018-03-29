import math
import numpy as np
from popilation_intit import population_init
from val_function import val_function
from decode_function import decode_function
from selection import selection
from crossover import crossover
from mutation import mutation


# 种群中个体数
Num = 200
# 个体中有多少个基因
DNA = 3
# 每个基因的取值范围
max = np.array([3, 2, 3])
min = np.array([-3, -2, -3])
# 要求的精度
J = np.array([1e-2, 1e-2, 1e-2])
# 种群个体的编码列表
encode = []
# 种群个体的解码列表
decode = []
# 求出要分多少个区间
area = (max - min)/J
# 求出需要用多少位来表示
Bit = np.modf(np.log2(area))[1]+1
# 交叉概率一般选择0.4-0.9
CV = 0.4
# 变异概率一般选择0.001-0.1
change = 0.05
# 目标函数列表
y = []
# 轮回多少代
epoch = 200


def run():
    # 初始化种群
    population_init(encode, Num, Bit)
    for i in range(epoch):
        # 解码
        decode = decode_function(encode, max, min, Bit)
        # 计算适应度(用直接以待求解的目标方程函数）
        y = val_function(decode)
        # 选择适应度提高的染色体进行复制
        selection(encode, y)
        # 交叉基因
        crossover(encode, CV, Bit)
        # 基因变异
        mutation(encode, change, Bit)



    #解码
    decode = decode_function(encode, max, min, Bit)
    # 新种群
    y = val_function(decode)
    a = 100-np.array(y).max()
    print(a)
    return a


if __name__ == "__main__":
    score_list = []
    for i in range(100):
        temp = run()
        score_list.append(temp)
        print(i, " : ", temp)
    #选择压力
    print(sum(score_list)/len(score_list))
