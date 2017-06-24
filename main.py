#!/usr/local/bin/python3

from produs import *
from random_tensor import *
from tensor import *
from tensor_unar import *
from produs_tensor_scalar import *

n = Tensor(2, 3, 3)
m = Tensor(2, 3, 3)
print("n", n)


n.tensor = random_tensor(n, 0, 5)
m.tensor = tensor_unar(2, 3)
print("n", n)
print("m", m)

p = produs_tensor_scalar(n, 2)
print("p", p)