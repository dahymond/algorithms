def reverse(words):

    if len(words) <= 1:
        return words

    return reverse(words[1:]) + words[1]


print reverse('ebunoluwa')