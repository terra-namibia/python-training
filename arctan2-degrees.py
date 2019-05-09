# coding: UTF-8
# 直角をはさむx=4,y=3の値(=比)から原点の角度を求める
import numpy as np

# 角度(ラジアン)を求める np.arctan2(y,x)
rad = np.arctan2(3,4)
# 角度をラジアン:弧度法から度数法に変換
th = np.degrees(rad)

print(rad)
print(th)

