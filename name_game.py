# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Shruti Ezhilarasan
# Section: 570
# Assignment: Lab 7- The Name Game
# Date: 26/9/2024

#get user input
x = input("What is your name? ")
y = x[0].lower()
count = 0

name = x[1:]

for letter in x:
    if letter.lower() in 'aeiou':
        break
    count += 1


#removes all beginning constanants      
name = x[count:]

#if the first letter is a vowel
if y in 'aeiou':
    name = y + x[1:]

#display output
print(f'{x}, {x}, Bo-B{name}')
print(f'Banana-Fana Fo-F{name}')
print(f'Me Mi Mo-M{name}')
print(f'{x}!')
