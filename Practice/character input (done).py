import datetime as dt

name = input('Enter your name ')

def numb():
    run = True
    while run:
        age = input('Enter your Age ' )
        y = age.isdigit()

        if y == True:
            run = False
        else:
            print()
            print('--------------')
            print('Enter a Number')
            print('--------------')
            print()

    age2 = int(age)
    return age2

#gathers date and time from computer
time = dt.datetime.now()
#takes current year on computer into an variable
year = time.year

#finds birth year of user
birth = year - numb()

#adds 100 to birth year to see what year they will be 100
old = birth + 100

print(f'{name} you will turn 100 in {old}')

print()
print()

#int variable that user enter
rep = int(input('Enter a random number '))

#int variable that will incerment until it hit user input number
num = 0

#repeats print statement until it hits user input number
while (num < rep):
    print(name,'you will turn 100 in',old,end='\n')
    num = num + 1 
