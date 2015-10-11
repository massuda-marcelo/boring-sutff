#! python

# Boring Stuff
# Ex 4-1 Comma Code

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(list):
    s = ''
    if len(list) > 0:
        for i in range(len(list) - 1):
            if len(s) > 0:
                s += ', '
            s += str(list[i])
        s += ' and ' + str(list[-1])
    s = '[' + s + ']'
    return s

print(comma_code(spam))
print(comma_code([]))
print(comma_code([1, 2, 3]))
