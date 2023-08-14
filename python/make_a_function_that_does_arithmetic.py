# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/

# Solution Submitted: 08/12/2023

def arithmetic(a, b, operator):
    result = 0

    if operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    elif operator == "multiply":
        result = a * b
    else:
        result = int(a / b)
    
    return result

# Solution Submitted: 08/12/2023

def arithmetic(a, b, operator):
    match operator:
        case 'add':
            return a + b
        case 'subtract':
            return a - b
        case 'multiply':
            return a * b
        case 'divide':
            return a / b
        case _:
            return f"operator '{operator }'' not found"

# User submitted solutions to review:

def arithmetic(a, b, operator):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]
       
def arithmetic(a, b, operator):
    dct = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }
    return eval(f'{a} {dct[operator]} {b}')


print(arithmetic(1, 2, "add")) # , 3, "'add' should return the two numbers added together!")
print(arithmetic(8, 2, "subtract")) #, 6, "'subtract' should return a minus b!")
print(arithmetic(5, 2, "multiply")) # , 10, "'multiply' should return a multiplied by b!")
print(arithmetic(8, 2, "divide")) # , 4, "'divide' should return a divided by b!")
print(arithmetic(8, 2, "mod"))

