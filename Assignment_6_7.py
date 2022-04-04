
def big_fibonacci(n):
    fibonacci = [1,1,2]
    while len(str(fibonacci[-1])) != n:
        a = int(fibonacci[-2]) + int(fibonacci[-1])
        fibonacci.append(a)
    return fibonacci[-1]

print(big_fibonacci(1))
print(big_fibonacci(2))
print(big_fibonacci(3))
print(big_fibonacci(5))
print(big_fibonacci(30))

        
        

  