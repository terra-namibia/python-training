# coding: UTF-8

import pandas as pd
import numpy as np

# csvデータを直接作成する方法
df = pd.DataFrame({
        'A' : [1, 2, 3],
        'B' : [30, 4, 8]
    })

#print(df)


# csvの読み込み
dat = pd.read_csv('score.csv', encoding='SHIFT-JIS')
# 内容を確認
df2 = dat.head()
print(df2)

# mathカラムの平均値 中央値
print('平均値', np.mean(dat['math']))
print('中央値', np.median(dat['math']))

# 最頻値 numpyで求める場合(mode()関数もあるが同じ度数が複数あるとエラーを返す)
bincnt = np.bincount(dat['math']) 	# 同じ値の個数を取得 [0 2 2 0 0 0 0 0 0 1]
mode = np.argmax(bincnt) 		# 最も大きな値の位置を取得
print(bincnt)
print('最頻値', mode)


