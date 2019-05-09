# coding: UTF-8

# (1,1) (5,3)の2点を結ぶ関数を求める y = a*x + b
# 1 = 1a + b  3 = 5a + b
from sympy import Symbol, solve # sympyの中から Symbolとsolveをimport


# 式を定義
a = Symbol('a')
b = Symbol('b')
ex1 = a + b - 1
ex2 = 5*a + b - 3

# 連立方程式を解く
print(solve((ex1, ex2)))
