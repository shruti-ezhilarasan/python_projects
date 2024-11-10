# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Saachi Jain
#               Clara Berg
#               Deepna Kanjee
#               Shruti Ezhilarasan
# Section:      570
# Assignment:   Lab: Topic 4 Pretty Equations
# Date:         9 September 2024


#Coefficients:
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))


#forumula = (f'{A} {plus} {B} {plus} {C} = 0')
sign = 0
#Coefficient A
if (A == 0):
    term1 = (f'')
elif (A == 1):
    term1 = (f'x^2')
    sign = 1
elif (A == -1):
    term1 = (f'- x^2')
    sign = -1
elif (A<0):
    term1 = (f'- {-A}x^2')
    sign = -2
else:
    term1 = (f'{A}x^2')
    sign = 2


#Coefficient B
if (B == 0):
    term2 = (f'')
elif (B == 1) and (sign != 0):
    term2 = (f' + x')
elif (B == 1):
    term2 = (f'x')
elif (B == -1):
    term2 = (f' - x')
elif (B<0):
    term2 = (f' - {-B}x')
elif (B>0) and (sign == 0):
    term2 = (f'{B}x')
else:
    term2 = (f' + {B}x')


#Coefficient C
if (C == 0):
    term3 = (f'')    
elif (C<0):
    term3 = (f' - {-C}')
else:
    term3 = (f' + {C}')


print(f'The quadratic equation is {term1}{term2}{term3} = 0')