''' Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion. '''

def power_fun(a,b):
    ''' function to calculate power of a raised by b'''
    if b==1:
        return a
    else:
        return a*power_fun(a,b-1)
a=int(input("Enter a in a**b: "))
b=int(input("Enter b in a**b: "))
print(power_fun(a,b))
