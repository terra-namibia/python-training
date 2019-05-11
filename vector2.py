# coding: UTF-8
# ベクトル 内積
# 直線AB:ベクトルa,CD:ベクトルbのなす角度を求める
import numpy as np
import math

# 座標
a = np.array([2,7])
b = np.array([6,1])
c = np.array([2,3])
d = np.array([6,5])

# ベクトルa,bの成分
va = b - a
vb = d - c

# ベクトルの大きさ
norm_a = np.linalg.norm(va)
norm_b = np.linalg.norm(vb)

# ベクトルの内積
dot_ab = np.dot(va, vb)

# 角度を求める
cos_th = dot_ab / (norm_a * norm_b)
rad = math.acos(cos_th)		# 角度に変換
deg = math.degrees(rad)		# 度数法に変換

print(deg)

