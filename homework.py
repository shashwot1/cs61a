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

#question 4
def largest_factor(x):
    for i in range(1,x):
        if(x%i==0):
            k=i
    return k        
print(largest_factor(49))

#question 5
def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result
        
        
def with_if_function():
    return if_function(3==0, true_func(), false_func())

def cond():
    return False

def true_func():
    print("Welcome to")

def false_func():
    print("61A")
    
with_if_function()

#question 6
def hailstone(x):
    print(x)
    while(x!=1):
        if(x%2==0):
            x=int(x/2)  # using `int` to explicitly define integer
            print(x)
        elif(x%2!=0):
            x=3*x+1
            print(x)
hailstone(10)

         

 