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