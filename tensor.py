#!/usr/local/bin/python3

# from number import *
from random import *

class Tensor:
	"""
	d = adincimea tenzorului
	y = numarul de linii
	x = munarul de coloane
	data = datele din tensorului
	f = functiile ce for fi aplicate
	dot = produsul dintre doi tensori prin metoda dot
	"""
	def __init__(self, d = 1, y = 1, x = 1, func = ['zero', '0'], parameter = [0, 0]):
		self.d = d
		self.y = y
		self.x = x
		self.data = 0
		self.f = 0
		lst_func = {'zero': (self.zero), 'null': (self.null), 'random': (self.random), 'unar': (self.unar)}
		lst_func[func[0]](func[1], parameter)

	def __str__(self):
		returnStr = "Tensor\n adincime: " + str(self.d) + "\n linii:    " + str(self.y)
		returnStr += "\n coloane:  " + str(self.x)
		returnStr += "\n" + str(self.data)
		return returnStr

	# Functii Publice-PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.
	# (public) ###### Functiile ce indeplinesc calculele matematice

	# ### Functia Pool
	def pool(t, func = 'max', size):
		lst_func = {'max': (self.max), 'min': (self.min), 'MA': (self.media_aritmetica)}
		self.f = lst_func[func]
		tensor = Tensor(self.d, self.y, self.x)
		tensor.data = self.adincime(0)
		return tensor
	# ### Functia Pool

	### Functia Transpusa
	def transpus(self):
		self.f = self.transpusa_ia
		x = self.x
		self.x = self.y
		y = self.y
		self.y = x
		tensor = Tensor(self.d, self.y, self.x)
		tensor.data = self.adincime(0)
		self.x = x
		self.y = y
		return tensor
	### Functia Transpusa

	# ### Functia Produs_dot
	def __mul__(self, t):
		if isinstance(t, Tensor):
			print("Tensor clas++++++++++++++++++++")
			if self.d != t.d or self.x != t.y:
				return
			self.f = self.dot
			tensor = Tensor(self.d, self.y, t.x)
			xp = self.x
			self.x = t.x
			tensor.data = self.adincime([t, xp])
			self.x = xp
			return tensor
		# if isinstance(t, number):
		self.f = self.produs_scalar
		tensor = Tensor(self.d, self.y, self.x)
		tensor.data = self.adincime(t)
		return tensor
	# ### Functia Produs_dot

	# ### Functia Suma
	def __add__(self, t):
		if self.d != t.d or self.x != t.x or self.y != t.y:
			return
		self.f = self.suma
		tensor = Tensor(self.d, self.y, self.x)
		tensor.data = self.adincime(t)
		return tensor
	# ### Functia Suma

	# ### Functia Produs pe element
	def produs(self, t):
		if self.d != t.d or self.x != t.x or self.y != t.y:
			return
		self.f = self.inmultire
		tensor = Tensor(self.d, self.y, self.x)
		tensor.data = self.adincime(t)
		return tensor
	# ### Functia Produs pe element

	# ### Functia Random
	def random(self, function, interval):
		self.f = self.random_tensor
		lst_func = {'uniform': (uniform), 'randint': (randint)}
		lst = [lst_func[function], interval]
		self.data = self.adincime(lst)
	# ### Functia Random

	### Functia Null
	def null(self, min, max):
		self.f = self.null_ia
		self.data = self.adincime(0)
	### Functia Null

	### Functia Unar
	def unar(self, min, max):
		self.f = self.unar_ia
		self.data = self.adincime(0)
	### Functia Unar

	### Functia Zero
	def zero(self, min, max):
		self.data = 0
	### Functia Zero
	# (public) ###### Functiile ce indeplinesc calculele matematice
	# Functii Publice-PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.PU.

	# ===================================================================================================================================

	# Functii Private-PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.
	# (privat) ###### Functiile ce indeplinesc un ciclu in adincime, pe linii si pe coloane+++++++++++++++
	def coloana(self, lst, dp, yp):
		return [ self.f(lst, dp, yp, i) for i in range(self.x) ]

	def linii(self, lst, dp):
		return [ self.coloana(lst, dp, i) for i in range(self.y) ]

	def adincime(self, lst):
		return [ self.linii(lst, i) for i in range(self.d) ]
	# (privat) ###### Functiile ce indeplinesc un ciclu in adincime, pe linii si pe coloane+++++++++++++++++

	# # (privat) ###### Functiile ce indeplinesc un ciclu in adincime, pe linii si pe coloane+++++++++++++++
	# 	def coloana_pas(self, lst, dp, yp):
	# 		return [ self.f(lst, dp, yp, i) for i in range(pas, self.x) ]

	# 	def linii_pas(self, lst, dp):
	# 		return [ self.coloana(lst, dp, i) for i in range(pas, self.y) ]

	# 	def adincime(self, lst):
	# 		return [ self.linii(lst, i) for i in range(self.d) ]
	# # (privat) ###### Functiile ce indeplinesc un ciclu in adincime, pe linii si pe coloane+++++++++++++++++

	# ===================================================================================================================================

	# (privat) ###### Functiile ce indeplinesc calculul asupra unui singur pixel

	# ### Functia Transpusa
	def transpusa_ia(self, lst, dp, yp, xp):
		return self.data[dp][xp][yp]
	# ### Functia Transpusa

	# ### Functia Null
	def null_ia(self, lst, dp, yp, xp):
		return 0
	# ### Functia Null

	# ### Functia Unar
	def unar_ia(self, lst, dp, yp, xp):
		if yp == xp:
			return 1
		return 0
	# ### Functia Unar

	# ### Functia Produs
	def inmultire(self, lst, dp, yp, xp):
		data = lst.data
		return self.data[dp][yp][xp] * data[dp][yp][xp]
	# ### Functia Produs

	# ### Functia Produs_scalar
	def produs_scalar(self, lst, dp, yp, xp):
		return self.data[dp][yp][xp] * lst
	# ### Functia Produs_scalar

	# ### Functia suma
	def suma(self, lst, dp, yp, xp):
		data = lst.data
		return self.data[dp][yp][xp] + data[dp][yp][xp]
	# ### Functia suma

	# ### Functia random (realizeaza un random cu numere intregi)
	def random_tensor(self, lst, dp, yp, xp):
		return lst[0](lst[1][0], lst[1][1])
	# ### Functia random 

	# ### Functia Produs Dot
	def dot(self, lst, dp, yp, xp):
		data = lst[0].data
		produs = 0
		for i in range(lst[1]):
			produs += self.data[dp][yp][i] * data[dp][i][xp]
		return produs
	# ### Functia Produs Dot

	# # ### Functia Isvalid
	def isvalid(self, t):
		pass
		# if isinstance(t, Tensor):
		# 	return 1
		# return 0
	# # ### Functia Isvalid

	# (privat) ###### Functiile ce indeplinesc calculul asupra unui singur pixel 
	# Functii Private-PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.PR.



