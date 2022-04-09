def is_prime(n):
    l = range(2, n, 1)
    for x in l:
        if n == 1:
            return False
        if n % x == 0:
            return False
    return True

 #Write a Python function called primes_below 
#that takes a number n and returns a list of all prime numbers less than n.

def primes_below(y):
    l = []
    for d in range(2,y):
        if is_prime(d):
            l.append(d)
    return l

print(primes_below(21))
