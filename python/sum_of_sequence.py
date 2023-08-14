# https://www.codewars.com/kata/586f6741c66d18c22800010a/

# Solution Submitted 08/13/2023
def sequence_sum(begin_number, end_number, step):
    # if begin_number > end_number: return 0

    result = []
    for i in range(begin_number, end_number + 1, step):
        # print(i)
        result.append(i)

    # print(result)
    return sum(result) # sum[] returns 0; no need for gaurd clause above

# Other users solutions
def sequence_sum(start, end, step):
    return sum(range(start, end+1, step))   


print(sequence_sum(2, 6, 2)) #, 12)
print(sequence_sum(1, 5, 1)) #, 15)
print(sequence_sum(1, 5, 3)) #, 5)
print(sequence_sum(0, 15, 3)) #, 45)
print(sequence_sum(16, 15, 3)) #, 0)
print(sequence_sum(2, 24, 22)) #, 26)
print(sequence_sum(2, 2, 2)) #, 2)
print(sequence_sum(2, 2, 1)) #, 2)
print(sequence_sum(1, 15, 3))# , 35)
print(sequence_sum(15, 1, 3))# , 0)