# coding: UTF-8

# サイコロを何度も振ったら最終的に1の目が出る確率は1/6になる
import random

# サイコロを振る
# random.randint(1, 6) 1-6までの整数のうちどれか一つをランダムに選ぶ
cnt = 0.0000
for i in range(10000):
  dice = random.randint(1, 6)
  if dice == 1:
    cnt += 1

# 確率を求める
p = cnt / 10000

print(p)

