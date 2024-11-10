# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Deepna Kanjee
#               Clara Berg
#               Saachi Jain
#               Shruti Ezhilarasan
# Section:      570
# Assignment:   Lab 11 TEAM - Passport Checker 2
# Date:         5 November 2024

file = input("Enter the name of the file: ")
count = 0
current_lines = []
valid_passwords = []


def valid_byr(value):
    return value.isdigit() and 1920 <= int(value) <= 2008


def valid_eyr(value):
    return value.isdigit() and 2024 <= int(value) <=2034


def valid_hgt(value):
    if len(value) > 2:
        unit = value[-2: ]
        height = value [ :-2]


        if unit == 'cm' and height.isdigit() and 150 <= int(height) <= 193:
            return True
        elif unit == 'in' and height.isdigit() and 59 <= int(height) <= 76:
            return True
    return False


def valid_hcl(value):
    return len(value) == 7 and value[0] == '#' and all(c in '0123456789abcdef' for c in value[1:])


def valid_ecl(value):
    return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def valid_pid(value):
    return value.isdigit() and len(value) == 9


def valid_cid(value):
    return value.isdigit() and len(value) == 3 and value [0] != '0'


field_valid = {
    "byr" :valid_byr, "eyr": valid_eyr, "hgt": valid_hgt, "hcl": valid_hcl, "ecl": valid_ecl, "pid": valid_pid, "cid": valid_cid
    }


def valid_passport(passport_data):
    fields = dict(field.split(":") for field in passport_data.split())
    required_fields = {"byr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    
    #all fields contain a value
    for field in required_fields:
        if field not in fields:
            return False

    return (
        valid_byr(fields["byr"]) and
        valid_eyr(fields["eyr"]) and
        valid_hgt(fields["hgt"]) and
        valid_hcl(fields["hcl"]) and
        valid_ecl(fields["ecl"]) and
        valid_pid(fields["pid"]) and
        valid_cid(fields["cid"])
    )


with open(file, 'r') as f:
    for line in f:
        if line == '\n':
            if current_lines:
                passport_text = ' '.join(' '.join(current_lines).split())
                if valid_passport(passport_text):
                    count += 1
                    valid_passwords.extend(current_lines)
                    valid_passwords.append('\n')
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        passport_text = ' '.join(' '.join(current_lines).split())
        if valid_passport(passport_text):
            count += 1
            valid_passwords.extend(current_lines)


print(f'There are {count} valid passports')

with open('valid_passports2.txt', 'w') as f:
    f.writelines(valid_passwords)

