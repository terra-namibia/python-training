# coding: UTF-8
# 行列 逆行列と単位行列
import numpy as np

# 行列a
a = np.matrix([[5, 3],[2, 1]])
# 行列aの逆行列bを求める
b = np.linalg.inv(a)
print(b)
print((b).astype(np.int64))

# a * bは単位行列になる
# そのままだと浮動小数点数型
print(a * b)
# 整数型に変換
print( (a * b).astype(np.int64) )

# bの値を直接設定
c = np.matrix([[-1, 3],[2, -5]])
print(a * c)

