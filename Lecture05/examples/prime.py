#! /usr/bin/env python

def gen_prime():
    pris = []
    i = 2
    while True:
        for p in pris:
            if i % p == 0:
                break
        else:
            pris.append(i)
            yield i
        i += 1

if __name__ == "__main__":
    primes = gen_prime() # get the generator
    for i in range(10):
        print(next(primes)) # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
