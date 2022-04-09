def is_prime(n):
    l = range(2, n, 1)
    for x in l:
        if n == 1:
            return False
        if n % x == 0:
            return False
    return n

list_1 = []
for x in range(10000,100000):
    if is_prime(x):
        if str(x) == str(x) [::-1]:
            list_1.append(x)
            print(list_1)


