import math
import sys
sys.setrecursionlimit (30000)
beg = eval(input("Enter the starting point N:\n"))              
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def prime(x, z):
    if z < 2:
        return False
    else: 
        if z**(1/2) >= x:
            if z == 2:
                return False
            elif (z%x) == 0:
                return False        
            else:
                return prime(x+1, z)
    return True
    
def palin(z):    
    z = str(z)
    if len(z) < 2:
        return True
    if z[0] != z[-1]:  
        return False
    else:
        return palin(z[1:-1]) 
      
def final(beg, end):
    if prime(2, beg):
        if palin(beg):
            print(beg)
    if beg<end:
        return final(beg+1, end)

final(beg, end)