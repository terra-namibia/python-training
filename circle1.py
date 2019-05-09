# coding: UTF-8
# 三角比を使って円を描画
import matplotlib.pyplot as plt
import numpy as np

# 角度
th = np.arange(0, 360, 1)
# 円周上の点の座標x,y (r * cos, r * sin)
r = 3	# 円の半径
x = r * np.cos(np.radians(th)) + 1	# +1:円の中心
y = r * np.sin(np.radians(th)) + 2	# +2:円の中心

# graph
plt.axis('equal')		# x/yのメモリ単位を揃える
plt.plot(x,y, color='blue')
plt.grid(color = '0.8')		# 背景のグリッド線描画
plt.show() 	# 画面表示

