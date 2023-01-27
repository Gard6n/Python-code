import sys 
#User input for numbers
try:
    Num = int(input('Give an number '))
    ran1 = int(input('Give number for start range '))
    ran2 = int(input('Give number for end range '))
except:
#If user enters not a number then program will exit
    print()
    print('Not a number boi')
    print()
    sys.exit()

ye = input('Do you want not Diveded? yes or no ')

num_list = []
num2_list = []

#Gives range to numbers to divide
for x in range(ran1,ran2):

#if its divsors number then its gets put into a new list
    if x%Num == 0:
        print()
        num_list.append(x)

#id its not a divsors number then its gets put into a new list
    if x%Num != 0:
     print()
     num2_list.append(x)

print(num_list)
print('Is divided')
print()

if ye.lower == 'yes':
    print(num2_list)
    print('Not Divded')
    print()
