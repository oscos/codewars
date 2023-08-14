# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/

# Created: 08/11/2023

def remove_smallest(l):
    ls = sorted(l)
    flag = True
    result = []

    for k in l:
        if k == ls[0] and flag:
            flag = False
            continue
        else:
            result.append(k)
    return result

# Solution Added 08/12/2023
def remove_smallest(l):
    lc = l.copy()

    if lc:
        lc.remove(min(lc))
    return lc

# Solution Added 08/12/2023
def remove_smallest(ls):
    if ls:
        mxn = ls.index(min(ls))
        p1 = ls[:mxn]
        p2 = ls[mxn + 1:]
        return p1 + p2
    else:
        return ls

# Solution Added 08/12/2023 - REFACTORED FROM ABOVE
def remove_smallest(ls):
    return ls[:ls.index(min(ls))] + ls[ls.index(min(ls)) + 1:] if ls else ls

print(remove_smallest([1, 2, 3, 4, 5])) # , [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
print(remove_smallest([5, 3, 2, 1, 4])) # , [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
print(remove_smallest([1, 2, 3, 1, 1])) # , [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
print(remove_smallest([])) #, [], "Wrong result for []")