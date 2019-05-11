# coding: UTF-8
# ベクトル
import numpy as np
import math

# a,b2点のベクトルの演算
a = np.array([2, 2])
b = np.array([2, -1])
print(a + b)
print(a - b)
print(2 * a)

# 10の力を別方向(60度)に加えた時のx軸に対する貢献度
# 結果は半分の5になる。なお30度にすると、約8の力となる
p = 10 * math.cos(math.radians(60))
print(p)

