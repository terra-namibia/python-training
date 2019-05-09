# coding: UTF-8

import matplotlib.pyplot as plt

# data
x = [1,2,3,4,5,6,7]
y = [64.3,63.8,63.6,64,63.5,63.2,63.1]

# graph
plt.plot(x,y, marker='o', color='red')	# marker:点を描画 color:線の色
plt.grid(color = '0.8')		# 背景のグリッド線描画
plt.show() 	# 画面表示

