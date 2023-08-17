# https://www.codewars.com/kata/539ee3b6757843632d00026b

def capitals(word):
    return [x for x, y in enumerate(word) if y == y.upper()]
    
# adapted from another users solution
# first convert string to list of indexes
# use element reference in anonymous function to to filter upper case char.
def capitals(word):
    return list(filter(lambda index: word[index].isupper(), range(len(word))))

print(capitals('CodEWaRs'), [0,3,4,6] )