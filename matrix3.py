# coding: UTF-8
# 逆行列で連立方程式を解く
# 5x + 3y =9
# 2x + y = 4
import numpy as np

# 行列a
a = np.matrix([[5, 3],[2, 1]])
# 行列aの逆行列を求める
inv_a = np.linalg.inv(a)

# 行列b
b = np.matrix([[9], [4]])

# 解x,y
print(inv_a * b)

