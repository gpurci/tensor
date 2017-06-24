#!/usr/local/bin/python3

def tensor_unar(d, n):
	return generare_3d(d, n)

def generare_1d(n, i):
	return [ diagonal_unar(i, j) for j in range(n) ]

def generare_2d(n):
	return [ generare_1d(n, i) for i in range(n) ]

def generare_3d(d, n):
	return [ generare_2d(n) for i in range(d) ]

def diagonal_unar(i, j):
	if i == j:
		return 1
	return 0