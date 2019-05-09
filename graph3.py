# coding: UTF-8
# 直線1に直交する直線2

import matplotlib.pyplot as plt
import numpy as np

# data
x = np.arange(-1, 6)	# x軸の範囲
y = 1/2.0 * x + 1/2.0	# 直線1
y2 = -2 * x + 7		# 直線1に直交する直線2

# graph
plt.axis('equal')		# x/yのメモリ単位を揃える
plt.plot(x,y, color='red')	# marker:点を描画 color:線の色
plt.plot(x,y2, color='blue')
plt.grid(color = '0.8')		# 背景のグリッド線描画
plt.show() 	# 画面表示

