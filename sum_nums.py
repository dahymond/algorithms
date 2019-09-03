def sumIntegers(arr, target):

    seen = set()

    for num in arr:

        num2 = target - num

        if num2 in seen:
            return True
        seen.add(num)
    return False



print sumIntegers([1,2,3,4,5,6,7], 14)


