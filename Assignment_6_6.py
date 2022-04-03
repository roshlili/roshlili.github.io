
def my_reverse(l):
    output = []
    while len(l) > 0:
        e = l[-1]
        output.append(e)
        l.pop(-1)
    return(output)

#l = [5,4,3,2,1]
#print(my_reverse(l))
print(my_reverse([5,4,3,2,1]))

