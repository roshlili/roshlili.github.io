#import math

def is_prime(n):
    l = range(2, n, 1)
    for x in l:
        if n == 1:
            return False
        if n % x == 0:
            return False
    return n

for x in range(1,100): #working check
    print(is_prime(x))