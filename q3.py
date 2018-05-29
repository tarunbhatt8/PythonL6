# Q.3- Print multiplication table of 12 using recursion.

def table(number,limit,t):
    ''' function to print the multiplication table of number uptil limit using recursion '''
    ''' indirectly it is a function to store the table of number uptil limit in a list t'''
    if limit==1:
        t.insert(0,number)

    else:
        t.insert(0,number*(limit))
        table(number,limit-1,t)

t=[]
table(12,10,t)
for i in t:
    print(i)
