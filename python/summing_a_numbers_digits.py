# https://www.codewars.com/kata/52f3149496de55aded000410/

def sum_digits(num):
    return sum([int(n) for n in str(abs(num))])


# Other solutions from users

# I liked this because of the math involved
# similar to how LS had me do it in Ruby without converting to digits or strings
def sumDigits(number):
    number = abs(number)
    return_number = 0
    
    while number > 0:
        return_number += number % 10
        number = int(number / 10)
        
    return return_number