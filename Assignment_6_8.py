range_1 = range(1, 1001, 1)
 
list_1 = list()
for x in range_1 :
    list_1.append(x)
 
#print(list_1) - we just made a list from 1 to 1000

for x in list_1:
    final_list = []
    if x % 5 == 0 and x % 3 == 0:
        final_list.append("FizzBuzz")
    elif x % 5 == 0:
        final_list.append("Buzz")
    elif x % 3 == 0:
        final_list.append("Fizz")
    else:
        final_list.append(x)
    print(final_list)