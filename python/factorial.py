# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc

def multiply(ls):
  prod = 1

  for x in ls:
    prod *= x
  
  return prod


def factorial(n):
  if n > 12 or n < 0:
    raise ValueError("Invalid Number")
  
  # ls = list(range(n + 1))[1:]
  ls = list(range(1, n + 1))

  return multiply(ls)

# Other user submission
import math
def factorial(n):
    if 0<=n<=12:
        return math.factorial(n)
    else:
        raise ValueError("value out of range")
    
# Other user submission
# the int("x") will always raise a value error that the problem asks for
# __import__("math") is another way of importing python modules to get it all in one line
factorial=lambda n:__import__("math").factorial(n)if 0<=n<13 else int("x")


print(factorial(0), 1, "factorial for 0 is 1")
print(factorial(1), 1, "factorial for 1 is 1")
print(factorial(2), 2, "factorial for 2 is 2")
print(factorial(3), 6, "factorial for 3 is 6")
print(factorial(4), 9, "factorial for 2 is 2")
print(factorial(5), 13, "factorial for 2 is 2")
# print(factorial(-1), "Error", "factorial for 0 is 1")