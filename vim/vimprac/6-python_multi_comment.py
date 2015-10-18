# Practice 6 - Python multiline comment

N = 100
a = [1 for i in range(N + 1)]
a[0] = a[1] = 0
prime = []

for i in range(N + 1):
	if a[i] == 1:
		prime.append(i)
		for j in range(i + i, N + 1, i):
			a[j] = 0
			print('{} is not a prime because {} divide it'
                              .format(j, i))
			print('Sometimes you would print', end = ' ')
			print('out some debug data.')
			print('You would have to comment out', end = ' ')
			print('those line afterward!')
			print('In python, comment start with #')
			# print('For example, this line has been commented')

print('There are {} primes in [1, {}]'.format(len(prime), N))
