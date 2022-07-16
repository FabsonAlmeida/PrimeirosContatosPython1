#This is file to calculate a second degree function using Py function

import math


import math

print("This application solve a second degree equation")

a=float(input("Type the A term"))
b=float(input("Type the B term"))
c=float(input("Type the C term"))

def f1(a, b, c):

    #Calculation
    x1=b*b-(4*a*c)
    x1=(-b+math.sqrt(x1))/2*a

    x2=float(b*b-(4*a*c))
    x2=float((-b-math.sqrt(x2))/2*a)

    return x1, x2

y,z=f1(a, b, c)

print("The returned values for X1 and X2 are:",y,z)