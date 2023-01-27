import sys

#user input for number
try:
    num = int(input('Enter a number '))
except:
    
#if user doesnt enter number program will exit
    print()
    print('Good Job you broke it!')
    print()
    sys.exit()

a = [1, 1, 3, 3, 5, 8, 13, 21, 34, 55, 89]
new = []

#interates through variable a 
for x in a:

#if number is more than user number it skips during interating
    if x > num:
        continue

#gets rids of other numbers thats not used and makes new list
    new.append(x)
    new.sort()

print(new)