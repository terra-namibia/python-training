# coding: UTF-8
# 三角形をx軸に対して線対称になるように移動

import numpy as np
import matplotlib.pyplot as plt

# 三角形ABCの頂点
p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1]])

# 変換行列 (x軸に線対称)
a = np.matrix([[1, 0], [0, -1]])

# 変換行列 (y軸に線対称)
b = np.matrix([[-1, 0], [0, 1]])

# 変換行列 (座標原点(0,0)に点対称)
c = np.matrix([[-1, 0], [0, -1]])


# 変換
p2 = a * p
p3 = b * p
p4 = c * p


print(p)
print(p2)
print(p3)
print(p4)

# 描画
p = np.array(p)
p2 = np.array(p2)
p3 = np.array(p3)
p4 = np.array(p4)

print(p)
print(p2)
print(p3)
print(p4)

plt.plot(p[0, :], p[1, :],  color='red')      # marker:点を描画 color:線の色
plt.plot(p2[0, :], p2[1, :],  color='blue')
plt.plot(p3[0, :], p3[1, :],  color='blue')
plt.plot(p4[0, :], p4[1, :],  color='blue')

plt.axis('equal')               # x/yのメモリ単位を揃える
plt.grid(color = '0.8')         # 背景のグリッド線描画
plt.show()      # 画面表示


