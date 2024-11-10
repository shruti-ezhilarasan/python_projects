# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Deepna Kanjee
#               Clara Berg
#               Saachi Jain
#               Shruti Ezhilarasan
# Section:      570
# Assignment:   Lab 3 Team- Unit Conversion
# Date:         9/8/24


paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost?"))
change = paid-cost
print(f'You received ${change:.2f} in change. That is...')




change*=100
change = round(change,2)
change = int(change)


#values
quarter = 25
dime = 10
nickel = 5
penny = 1


if((change//quarter) !=0):
   if((change//quarter) == 1):
       print(f'{change//quarter} quarter')
   if((change//quarter) > 1):
       print(f'{change//quarter} quarters')
   change = change%quarter


if((change//dime) !=0):
   if((change//dime) == 1):
       print(f'{change//dime} dime')
   elif((change//dime) > 1):
       print(f'{change//dime} dimes')
   change = change%dime


if((change//nickel) !=0):
   if((change//nickel) == 1):
       print(f'{change//nickel} nickel')
   elif((change//nickel) > 1):
       print(f'{change//nickel} nickels')
   change = change%nickel


if((change/penny) !=0):
   if((change/penny) == 1):
       print(f'{change//penny} penny')
   if((change//penny) > 1):
       print(f'{change//penny} pennies')
   change = change%penny