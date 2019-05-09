# coding: UTF-8

# 2直線の交点を求める
# y = -3/2x + 6 , y = 1/2x + 2
from sympy import Symbol, solve # sympyの中から Symbolとsolveをimport

# 式を定義
x = Symbol('x')
y = Symbol('y')
ex1 = -3.0/2*x + 6 - y
ex2 = 1.0/2*x + 2 - y

# 連立方程式を解く
print(solve((ex1, ex2)))
