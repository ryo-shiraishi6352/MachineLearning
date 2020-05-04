import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7 # 対数の真数が0のとき-infになるので微小な値を足す
    return -np.sum(t * np.log(y + delta))

# 2が正解
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# 2の確率が最も高い
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
print(cross_entropy_error(np.array(y), np.array(t))) 

# 7の確率が最も高い
y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
print(cross_entropy_error(np.array(y), np.array(t))) 
