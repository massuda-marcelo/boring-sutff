#! python
#  encoding: utf-8

# Boring Stuff
# Ex 4-2 Character Picture Grid

grid = [
    [ '.', '.', '.', '.', '.', '.' ],
    [ '.', '0', '0', '.', '.', '.' ],
    [ '0', '0', '0', '0', '.', '.' ],
    [ '0', '0', '0', '0', '0', '.' ],
    [ '.', '0', '0', '0', '0', '0' ],
    [ '0', '0', '0', '0', '0', '.' ],
    [ '0', '0', '0', '0', '.', '.' ],
    [ '.', '0', '0', '.', '.', '.' ],
    [ '.', '.', '.', '.', '.', '.' ]
]

for row in range(len(grid[0])):
    for col in range(len(grid)):
        print(grid[col][row], end='')
    print('')

