
from typing import KeysView

def to_hex(n):
    if n <= 255:
        #bla bla
        output = []
        d = {10: "A" ,11:"B" ,12:"C", 13:"D", 14:"E", 15:"F"}
        a = n//16 #full
        b = n % 16 #remainder
        output.append(b) #append 
        output.append(a) #append 
        while b != 0:
            b = a % 16
            a = a//16
            output.append(b) #append
        output.reverse()
    if len(output) > 1:
            output.pop(0)
        result = ""
        for x in output:
            if x > 9 and x < 16:
                result += d.get(x)
            else:
                result += str(x)
        return result

print(to_hex(10))
print(to_hex(32))
print(to_hex(255))
print(to_hex(16))

def hex_color(red,green,blue):
    trueresult = "#"
    truered = to_hex(red)
    trueresult += truered
    truegreen = to_hex(green)
    trueresult += truegreen
    trueblue = to_hex(blue)
    trueresult += trueblue
    return trueresult

print(hex_color(10,32,255)) 





    
    
    
    
    
    
