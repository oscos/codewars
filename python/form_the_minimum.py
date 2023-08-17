
# Solution 1
import itertools

def min_value(digits):
    digits_set = set(digits)
    com_set = itertools.combinations(digits_set, len(digits_set))
    for i in com_set:
        com_list = sorted(list(i))
        return int("".join(map(str, com_list)))


# refactored after seeing other solutions:
def min_value(digits):
    digits_set = sorted(set(digits))
    return int("".join(map(str, digits_set)))

# Other's solutions
def min_value(digits):
     return int("".join(map(str,sorted(set(digits)))))

# Other's Solution
def min_value(digits):
    return int("".join(str(x) for x in sorted(set(digits))))

# Other's Solution
minValue = lambda a: int(''.join(sorted(str(c) for c in set(a))))

print(min_value([1, 3, 1]), 13)
print(min_value([4, 7, 5, 7]), 457)
print(min_value([4, 8, 1, 4]), 148)