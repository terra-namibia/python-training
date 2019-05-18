# coding: UTF-8
# 集合
# import numpy as np

a = { 1,2,3,4,5,6,7,8,9 }
b = { 1,3,9,4,5,6,7,8,2 }

print(a == b)

# 要素数
print(len(a))

# 要素追加
a.add(10)
print(len(a))

# 部分集合:bがaに含まれるか確認
print(a <= b)

# 積集合
print(a & b)

# 和集合
print(a | b)

# 差集合
print(a - b)

# 対象差
print(a ^ b)

# 空集合
x = { 1,2 }
y = { 3,4 }
print(x & y)


