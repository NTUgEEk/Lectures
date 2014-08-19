# Practice 11 - Python Fix !
# :[%..]s/[pat1]/[pat2]/[flag] - subsitute
# Oops! A careless programmer forget
# To add the argument 'self' in every
# class function!
# In python, Class functions MUST be
# like
# def func_name(self, arg1, arg2 ...)
# and you'll call like
# func_name(arg1, arg2, ...)
# Python will automatic pass 'self'
# for you !!
# Fix all the class function by
# using :s !!!
# hint1: reg expression
# . : any character 
# * : match any times 
# \( ... \) : group
# \1 : first group
# \2 : second group
# hint2: functions start with def

class Vim:

	def __init__():
		self.name = 'Vim'
		self.sep = ' '

	def printVim():
		print(self.name, end=' ')

	def printo(a):
		for i in range(a):
			print('o', end='')

	def printis():
		print('is', end = '')

	def printsp(time, sep = ' '):
		for i in range(time):
			print(sep, end='')

	def printoh(c):
		for i in range(c):
			print('!', end='')

	def printcool(b, d):
		print('c', end='')
		self.printo(b)
		print('l', end='')
		self.printoh(d)

	def printsen(x = 6, y = 4):
		self.printVim()
		self.printis()
		self.printsp(1)
		self.printcool(x, y)


a = Vim()
a.printsen()
