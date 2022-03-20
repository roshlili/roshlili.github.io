import math

def solve_quadratic(a,b,c):
    d = b*b-(4*a*c)
    if (d > 0):
        x = (-b + math.sqrt(d))/2*a
        y = (-b - math.sqrt(d))/2*a
        print (x,y)
    elif (d == 0):
        x = (-b + math.sqrt(d))/2*a
        print (x)
    else:
        print ('none')

solve_quadratic(1,-5,6)
solve_quadratic(1,4,4)
solve_quadratic(1,0,1)
