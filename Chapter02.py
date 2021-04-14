
x = 1
y = 12
def g1(x):
    def g2(x):
        print(x)
    g2(x + 1)
g1(2)

def square(x):
    return x*x
def sum_square(x,y):
    return square(x)+square(y)
z=sum_square(3,4)
print(z)        

def id(x):
    return x
print(id(id)(id(13)))

def sum_seq(k,i,x):
    if(i>x):
        print(k)
    else:
        sum_seq(k+square(i),i+1,x)
sum_seq(0,1,100)

def is_prime(x):
    if(x>1):
        if(x%2==0):
            print(x,"is not a prime")
        else:    
          for i in range (3,x):       
              if(x%i==0):
                  #print(x,"is not a prime")
                  return False
              else:
                  continue
          if(True):
                #print(x,"is  a prime")    
                return True

#not complete     
def print_primefactor(x):
    k=1     
    while(k<x):
        if(x%2==0):
            print(2)
            x=x/2
        else:    
         for i in range(3,x):
             if(x%i==0):
                 if(is_prime(i)):
                     print(i)
                     k=k*i


print_primefactor(14)                