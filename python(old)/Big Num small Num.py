
loop = 1

while loop == 1:
    wow = int(input('Enter 2 '))
    if wow == 2:
        people = [
            "Stephanie 36",
            "John 29",
            "Emily 24",
            "Gretchen 54",
            "Noah 12",
            "Penelope 32",
            "Michael 2",
            "Jacob 10"
        ]

        really_big = people[0]

        for big in people:
            if big > really_big:
             really_big = big
             print(f'{really_big}')

   