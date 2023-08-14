# https://www.codewars.com/kata/545a4c5a61aa4c6916000755

# Solution submitted: 08/12/2023
def gimme(input_array):
    ls = sorted(input_array)
    return input_array.index(ls[1])
    
# refactored
def gimme(input_array):
    m = sorted(input_array)[1]
    return input_array.index(m)
