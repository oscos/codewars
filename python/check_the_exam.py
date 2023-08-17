def check_exam(arr1, arr2):
    points = []

    for k, v in enumerate(arr1):
        # print("k =>", k, ": v =>", v)
        if arr2[k] == "":
          points.append(0)
        elif v == arr2[k]:
            points.append(4)
        elif v != arr2[k]:
            points.append(-1)
    
    total = sum(points)

    return 0 if total < 0 else total


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7)
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0)


# Other user submissions to review:
def check_exam(arr1, arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))

