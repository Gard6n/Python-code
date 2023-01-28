import sys
loop = 1
while loop == 1:
    user = int(input('Enter 1 to open file or 2 to kill program '))
    if user == 1:
        with open('books.txt') as mormon:
            for mormons in mormon:
                nice = mormons.strip()
                print(f'{nice}')

    if user == 2:
        sys.exit()
