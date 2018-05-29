''' Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary '''

def factorial(num):
    ''' function to find factorial of a number'''
    if num<=1:
        return 1
    else:
        return num*factorial(num-1)

dict={}

ch='y'

while ch=='y':

    n=int(input("Enter number to find factorial of: "))

    f=factorial(n)

    dict[n]=f

    ch=input("Do you want to find more factorials?? y/n : ")

print("The dictionary for all your inputs and their factorials are as follows: ")
print(dict)
