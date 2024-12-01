def get_valid_letters(puzzle_str):
    unique_lt = ""
    for char in puzzle_str:
        #check if alphabetic charcters are considered and prevent duplicate letters added to "unique_ly"
        if (char.isalpha()) and (char not in unique_lt):
            #adds the charcter to "unique_lt"
            unique_lt += char
    return unique_lt


def is_valid_guess(unique_lt, user_guess):
    if len(user_guess) != 10:
        return False
    unique_user_lt = " "
    for char in user_guess:
        if (char in unique_lt) and (char not in unique_user_lt):
            unique_user_lt += char
        else:
            return False    
    return True


def check_user_guess(dividend, quotient, divisor, remainder):
    return( dividend == (quotient * divisor + remainder))


def make_number (word_int, user_guess):
    int_convert = ""
    for char in word_int:
        int_convert += str(user_guess.index(char))
    return int(int_convert)


def make_numbers(puzzle_str, user_guess):
    #splitting the quoteint, divisor, dividend, & remainder
    puzzle_list = puzzle_str.split(",")
    #slpits divisor & dividend @ |
    d_d = puzzle_list[1]
    puzzle_list[1] = d_d[0: d_d.index(" ")]
    puzzle_list.insert(2, d_d[d_d.index(" ")+3:])


    quoteint = puzzle_list[0]
    divisor = puzzle_list[1]
    dividend = puzzle_list[2]
    remainder = puzzle_list[-1]


    int_dividend = make_number(dividend, user_guess)
    int_quotient = make_number(quoteint, user_guess)
    int_divisor = make_number(divisor, user_guess)
    int_remainder = make_number(remainder, user_guess)


    return(int_dividend, int_quotient, int_divisor, int_remainder)


def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")


def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    print("Enter a word arithmetic puzzle: ")
    puzzle_str = input()
    print_puzzle(puzzle_str)
    print()
    print("Enter your guess, for example ABCDEFGHIJ: ", end="")
    user_guess = input()


    valid_lt = get_valid_letters(puzzle_str)
    if (is_valid_guess(valid_lt, user_guess)):
        numbers = make_numbers(puzzle_str, user_guess)
        if(check_user_guess(numbers[0], numbers[1], numbers[2], numbers[3])):
            print("Good job!")
        else:
            print("Try again!")
    else:
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")




if __name__ == '__main__':
    main()
