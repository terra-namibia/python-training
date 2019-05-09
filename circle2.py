# coding: UTF-8
# 三平方の定理を使って円を描画　中心は0,0で上側の半円の場合
import matplotlib.pyplot as plt
import numpy as np

r = 300	# 円の半径
x = np.arange(-r, r+1)		# -300から300
y = np.sqrt(r**2 - x**2)	# 円の方程式

# graph
plt.axis('equal')		# x/yのメモリ単位を揃える
plt.plot(x,y, color='blue')
plt.grid(color = '0.8')		# 背景のグリッド線描画
plt.show() 	# 画面表示

