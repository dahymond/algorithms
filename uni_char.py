'''def uni_char(s):
    return len(set(s)) == len(s)

print uni_char('acbsd')    
'''

def uni_char(s):

    chars = set()

    for letter in s:

        if letter in chars:
            return False
        else:
             chars.add(letter)   

    return True

print uni_char('acbsd')

