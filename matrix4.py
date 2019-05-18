# coding: UTF-8
# ベクトル（点P）と行列の掛け算=>新たな点(座標Q)が求められる

import numpy as np

# 点P
P = np.matrix([[3],[2]])

# 行列A
A = np.matrix([[2, 0], [1, 2]])

# 新たな座標Q
print(A * P)

