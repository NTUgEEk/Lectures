# Practice 6 - Python multiline comment

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
