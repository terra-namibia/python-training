# coding: UTF-8

# 順列
import itertools

num = { 1,2,3,4,5 }
# numから3つを選ぶ順列で集合を生成 順列なので同じ数字は使えない<=>重複順列(112なども可)
A = set(itertools.permutations(num, 3))
# numから3つを選ぶ重複順列
# A = set(itertools.product(num, num, num))


# Aの要素数 60通り
print(len(A))
print(A)

#for a in A:
# print(a)

