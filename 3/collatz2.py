#! python3

# Boring Stuff
# Ex 3-1 The Collatz Sequence

s = input('Enter number: ')
try:
    n = int(s)
except ValueError:
    print('Error: ' + s + ' is an invalid number')
    exit()

while (n > 1):
    if (n % 2 == 0):
        n = (n // 2)
    else:
        n = (3 * n + 1)
    print(str(n))
