# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Deepna Kanjee
#               Clara Berg
#               Saachi Jain
#               Shruti Ezhilarasan
# Section:      570
# Assignment:   Lab 8 Team- ASCII Clock
# Date:         17 October 2024
 


# Dictionary to represent each digit and letters (A, M, P) in 3x5 ASCII art
digits = {
    '0': ['000', '0 0', '0 0', '0 0', '000'],
    '1': [' 1 ', '11 ', ' 1 ', ' 1 ', '111'],
    '2': ['222', '  2', '222', '2  ', '222'],
    '3': ['333', '  3', '333', '  3', '333'],
    '4': ['4 4', '4 4', '444', '  4', '  4'],
    '5': ['555', '5  ', '555', '  5', '555'],
    '6': ['666', '6  ', '666', '6 6', '666'],
    '7': ['777', '  7', '  7', '  7', '  7'],
    '8': ['888', '8 8', '888', '8 8', '888'],
    '9': ['999', '9 9', '999', '  9', '999'],
    ':': [' ', ':', ' ', ':', ' '],
    'A': [' A ', 'A A', 'AAA', 'A A', 'A A'],
    'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M'],
    'P': ['PPP', 'P P', 'PPP', 'P  ', 'P  ']
}


# Get user input
time = input("Enter the time: ")
clock_type = input("Choose the clock type (12 or 24): ")


# List of allowed characters for replacement
allowed_c = 'abcdeghkmnopqrsuvwxyz@$&*='
preferred_c = input("Enter your preferred character: ")


# Keep asking for a valid character
while preferred_c not in allowed_c and preferred_c != '':
   
    print("Character not permitted! Try again: ", end='')  # Suppress newline
    preferred_c = input()
   
# Split time input into hours and minutes
hours, minutes = time.split(':')


# If 12-hour format, convert the time and add AM/PM
period = ''
if clock_type == '12':
    hours = int(hours)
    if hours == 0:
        period = "AM"
        hours = 12
    elif hours < 12:
        period = "AM"
    else:
        if hours > 12:
            hours -= 12
        period = "PM"
    hours = str(hours)


# Remove leading zero for 12-hour clock format if hours > 9
if clock_type == '12' and len(hours) == 2 and hours.startswith('0'):
    hours = hours[1]  # Remove the leading zero


# Create ASCII art for the digits
ascii_art = ['', '', '', '', '']  # 5 lines for ASCII art


for char in hours + ':' + minutes:
    if char != ':':
        if preferred_c == '':
            # If preferred character is a space, print the actual number
            digit_art = digits[char]
        else:
            # Replace all characters with the preferred character
            digit_art = [line.replace(char, preferred_c) for line in digits[char]]
            # Replace all other characters in the line with preferred character too
            digit_art = [line.replace('0', preferred_c).replace('1', preferred_c).replace('2', preferred_c)
                              .replace('3', preferred_c).replace('4', preferred_c).replace('5', preferred_c)
                              .replace('6', preferred_c).replace('7', preferred_c).replace('8', preferred_c)
                              .replace('9', preferred_c) for line in digit_art]
    else:
        # Handle colons (:) separately
        digit_art = digits[':']
   
    # Add each line of the current digit's ASCII art to the corresponding line in ascii_art
    for i in range(5):
        ascii_art[i] += digit_art[i] + ' '  # Ensure proper spacing


# If 12-hour format, append "AM" or "PM" to the time in ASCII art
if clock_type == '12':
    for char in period:
        letter_art = digits[char]  # Get ASCII art for 'A', 'M', or 'P'
        for i in range(5):
            ascii_art[i] += letter_art[i] + ' '  # Append letter with proper spacing


# Print the ASCII art for the time
print()
for line in ascii_art:
    print(line[:-1])  # Print each line without the trailing space
