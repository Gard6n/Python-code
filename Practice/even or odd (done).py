
while True:
    #gets input numbers from user
    user_num = input('Enter a number ')
    check = input('Enter a number to check ')
    divide = input('Enter a number to divide ')

    #checks if input from user has numbers in it and makes it a bool T or F
    user_numL = user_num.isdigit() and check.isdigit() and divide.isdigit()

    #sees if user_numL is False, if it is then repeats from the beginging 
    if user_numL == False:
        print()
        print('Thats not a number')
        print()
    else:
        break

#convets all str to ints
user_num = int(user_num)
check = int(check)
divide = int(divide)

#sees if user_num divides evenly into 2
if user_num%2 == 0:
    print()
    print('Thats a even number')

else:
    print()
    print('Thats a odd number')

#sees if the user number divides evenly, no remainder
if (check%divide) == 0:
    print()
    print('it divides evenly ')
else:
    print()
    print('It does not divide evenly')
    print()
