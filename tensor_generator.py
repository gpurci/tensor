#!/usr/local/bin/python3

def generare_1d(x, lst):
	return [ lst[2](lst[0], lst[1]) for i in range(x) ]

def generare_2d(y, x, lst):
	return [ generare_1d(x, lst) for i in range(y) ]

def generare_3d(d, y, x, lst):
	return [ generare_2d(y, x, lst) for i in range(d) ]