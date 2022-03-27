from re import M

def my_range(m,n):
    output = []
    while m <= n-1:
        output.append(m)
        m = m+1
    return output

my_range(1,5)
