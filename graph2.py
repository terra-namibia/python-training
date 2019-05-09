# coding: UTF-8

import matplotlib.pyplot as plt
import numpy as np

# data
x = np.arange(-2.0, 2.01, 0.01)	# -2から2までの値が0.01間隔で代入
y = 3 * x
y2 = 3 * x*x
y3 = 3 * x*x*x

# graph
plt.plot(x,y, marker='o', color='red')	# marker:点を描画 color:線の色
plt.plot(x,y2, marker='o', color='blue')
plt.plot(x,y3, marker='o', color='green')
plt.grid(color = '0.8')		# 背景のグリッド線描画
plt.show() 	# 画面表示

