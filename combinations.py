# coding: UTF-8

# 組み合わせ
import itertools
import math

num = { 1,2,3,4,5 }
# numから3つを選ぶ組み合わせ
A = set(itertools.combinations(num, 3))
print(len(A))
print(A)

