# Q.1- Create a function to calculate the area of a sphere by taking radius from user.
def area_sphere(r):
    '''Function to calculate area of a sphere using radius'''
    return ((4/3)*(3.14)*(r**3))

radius=float(input("Enter radius of sphere: "))
print("Area of sphere with radius {} = {}".format(radius,area_sphere(radius)))
