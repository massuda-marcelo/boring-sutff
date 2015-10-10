#! python3

# Boring Stuff
# Ex 3-1 The Collatz Sequence

def collatz(n):
    if (n % 2 == 0):
        return (n // 2)
    else:
        return (3 * n + 1)

s = input('Enter number: ')
try:
    n = int(s)
except ValueError:
    print('Error: ' + s + ' is an invalid number')
    exit()

while (n > 1):
    n = collatz(n)
    print(str(n))
