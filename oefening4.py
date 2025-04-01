nums = [1,3,4,-2,-4,6]
target = 3

def countTargetPairs(lijst, target):
    resultaat = 0
    i = 0
    for x in lijst:
        j = 0
        for y in lijst:
            if x + y < target and i < j:
                resultaat += 1
            j += 1
        i += 1
    return resultaat

print(countTargetPairs(nums, target))
