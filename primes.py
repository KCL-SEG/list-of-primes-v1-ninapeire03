"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(n):
    isPrime = True
    for i in range (2,n):
        if n%i == 0:
            isPrime = False
    return isPrime

def primes(number_of_primes):
    list = [2]
    n = 3
    while (len(list) < number_of_primes):
        if isPrime(n):
            list.append(n)
        n += 1
    return list
