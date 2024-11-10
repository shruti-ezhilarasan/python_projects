# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Deepna Kanjee
#               Clara Berg
#               Saachi Jain
#               Shruti Ezhilarasan
# Section:      570
# Assignment:   Lab 11 Team- Passport checker
# Date:         31 October 2024




filename = input("Enter the name of the file: ") # asks for file
passports = open(filename, "r") # opens the file and reads it


# creates a new file to write the vaild passports to the file
valid_file = open("valid_passports.txt",'w')


passportstring = passports.read().split("\n\n")# read the lines and remove \n


#the required field needed for each passport:
fields = ["byr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]



v_passports = []


#loops though the passport in the list of passportstring
for passport in passportstring:
    #Checks if the valid fields in the passport are present
    if all(i in passport for i in fields):
        # if all the required fields are present then the passport is valid and append to valid passports list
        v_passports.append(passport)


# writes the valid passports to the file
for v_passport in v_passports:
    valid_file.write(v_passport + '\n\n')  


# prints out the amount of valid of passport there are
print(f"There are {len(v_passports)} valid passports")




passports.close()
valid_file.close()





