def rem_duplicate(words):

    if len(words) <= 1:
        return words

    result = []
    seen = set()

    for letters in words:

        if letters not in seen:
            seen.add(letters)
            result.append(letters)

    return ''.join(result)


print rem_duplicate('Solomon sunday')



def duplicate_removal_list(arr):
    
    if len(arr) <= 1:
        return ValueError

    result = []

    seen = set()

    for numb in arr:

        if numb not in seen:
            seen.add(numb)
            result.append(numb)


    return result


print duplicate_removal_list([1,2,3,4,4,4,5,6,8])

print duplicate_removal_list([1,12,12,13,13,14,1,4,4,5,6,8])
