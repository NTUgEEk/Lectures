#! /usr/bin/env python

from prime import gen_prime
from mod.point import Point

primes = gen_prime()
p10 = []
for i in range(10):
    p10.append(next(primes))

print(', '.join(map(str,p10))) # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

a = Point(2, 4)
b = Point(-3, 6)
print(a - b)
a += b
print(a)
b -= a
print(-b)
