#question 2
from operator import abs
print(abs(-5))

def a_plus_abs_b(a,b):
    if b < 0:
        return a-b
    else:
        return a+b

print(a_plus_abs_b(1,-2))
print(a_plus_abs_b(1,2))

#question 3
def two_of_three(x,y,z):
    if (x>y & x>z):
        return y*y+z*z
    elif(y>x & y>z):
        return x*x+z*z
    else:
       return x*x+y*y    
print(two_of_three(3,2,1)) 
print(two_of_three(3,4,5)) 
print(two_of_three(8,10,6))        
 