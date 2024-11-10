# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Shruti Ezhilarasan
# Section: 570
# Assignment: Lab 4- Calculate roots
# Date: 12/9/24

from math import *

# user inputs

a = int(input("Please enter the coefficient A: "))
b = int(input ("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

# quadratic formula
inner = (b**2)-(4*a*c)

if (a == 0) and (b == 0):
    print ("You entered an invalid combination of coefficients!")
elif (a == 0):
    x = -c/b
    print (f'The root is x = {x}')
elif (inner < 0):
    outer = -b/ 2*a
    x1 = ( (-b)+(sqrt(-inner)))/(2*a)
    x2 = ((-b) -(sqrt(-inner)))/(2*a)
    if (x1 == 0):
        print(f'The root is x = {outer} - {x2}i')
    elif (x2 == 0):
        print(f'The root is x = {outer} + {x1}i')
    elif (x1 == x2):
        print (f'The root is x = {outer} + {-x1}i')
    else:
        print (f'The roots are x = {outer} + {-x1}i and x = {outer} - {-x1}i')
else:
    
    x1 = ( (-b)+(sqrt(inner)))/(2*a)
    x2 = ((-b) - (sqrt (inner) ))/(2*a)
    
    if (x1 == 0):
        print(f'The root is x = {x1}')
    elif (x2 == 0):
        print(f'The root is x = {x2}')
    elif (x1 == x2):
        print(f'The root is x = {x1}')
    else:
        print(f'The roots are x = {x1} and x = {x2}')
