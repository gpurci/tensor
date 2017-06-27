#!/usr/local/bin/python3

from produs import *
from random_tensor import *
from tensor import *
from tensor_unar import *
from produs_tensor_scalar import *
from produs_tensor_matrix import *
from tensor_transpus import *
from tensor_putere import *

n = Tensor(1, 3, 3)
m = Tensor(1, 3, 3)
# print("n", n)


n.tensor = random_tensor(n, 0, 5)
m.tensor = random_tensor(m, 0, 5)
print("n", n)
print("m", m)

p = produs_tensor(n, m)
# p = produs_tensor_scalar(n, 2)
# print("produs cu un scalar", p)
# p = produs_tensor_matrix(n, m)
print("produs matrice", p)
p = tensor_putere(n, 3)
print("putere matrice", p)
