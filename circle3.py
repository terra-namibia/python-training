# coding: UTF-8
# 三平方の定理を使って円を描画 中心が200,300で上側/下側両方の円を描画
import matplotlib.pyplot as plt
import numpy as np

r = 300	# 円の半径

# 円の中心
a = 200
b = 300

# 円の方程式
x = np.arange(a-r, a+r+1)		# -100から500の円となる
y = np.sqrt(r**2 - (x-a)**2) + b	# 円の上側
y2 = -y + 2*b				# 円の下側

# graph
plt.axis('equal')		# x/yのメモリ単位を揃える
plt.plot(x,y, color='blue')
plt.plot(x,y2, color='green')
plt.grid(color = '0.8')		# 背景のグリッド線描画
plt.show() 	# 画面表示

