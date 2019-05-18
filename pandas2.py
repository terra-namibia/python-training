%matplotlib inline
# coding: UTF-8


import pandas as pd
import matplotlib.pyplot as plt

# csvデータを直接作成する方法
df = pd.DataFrame({
        'A' : [1, 2, 3],
        'B' : [30, 4, 8]
    })

#print(df)


# csvの読み込み
dat = pd.read_csv('score2.csv', encoding='SHIFT-JIS')

# 内容を確認
print(dat)

df2 = dat.head()
print(df2)

# 各階級に含まれる度数を数える
hist = [0]*10
print(hist)

for dat in dat['math']:
  if dat < 10: hist[0] += 1
  elif dat < 20: hist[1] += 1
  elif dat < 30: hist[2] += 1
  elif dat < 40: hist[3] += 1
  elif dat < 50: hist[4] += 1
  elif dat < 60: hist[5] += 1
  elif dat < 70: hist[6] += 1
  elif dat < 80: hist[7] += 1
  elif dat < 90: hist[8] += 1
  elif dat <= 100: hist[9] += 1
print('度数:', hist)

# 度数分布図
x = list(range(1,11))	# x軸の値
labels = ['0-','10-','20-','30-','40-','50-','60-','70-','80-','90-']	# x軸のラベル
plt.bar(x, hist, tick_label=labels, width=1)	# 棒グラフ描画
plt.show

