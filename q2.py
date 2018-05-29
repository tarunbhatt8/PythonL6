''' Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3]. '''

def perfect(number):
    '''function to determine if the parameter is perfect, i.e if it's factors sum up to be the number itself'''
    num=0
    for i in range(1,number):
        if number%i==0:
            num+=i
    else:
        if num==number:
            return True
    return False

for i in range(1,1000):
    if perfect(i):
        print(i)
