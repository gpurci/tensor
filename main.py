#!/usr/local/bin/python3

from tensor import *
from Perceptron import *

n = Tensor(1, 1, 3, ['random', 'uniform'], [0, 5])
m = Tensor(1, 3, 1, ['random', 'uniform'], [0, 5])
print("n", n)
print("m", m)
p = n * m
print("p", p)
p = n * 2
print("p", p)
# s = n + m
# print("s", s)
# t = n.produs(m)
# print("t", t)
# print("n", n)
# tu = t.transpus()
# print("tu", tu)
Per = Perceptron([2, 3, 1])
print("Perceptron ", Per)


