#!/usr/local/bin/python3

from produs_tensor_matrix import *

def tensor_putere(t, p):
	n = t
	p = p - 1
	for i in range(p):
		n = produs_tensor_matrix(n, t)
		print("putere", i, n)
	return n