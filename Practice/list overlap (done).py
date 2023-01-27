import random as ra

#Empty lists
li = []
li2 = []

#function that prints out random numbers for range   
def dom():

    while True:
        b = ra.randint(1,10)
        c = ra.randint(10,25)

        f = range(b,c)
        break
    return f

#Makes a list of random numbers and amount of numbers
li = [x for x in dom()]

li2 = [b for b in dom()]

print(li)
print('Set 1')
print()
print(li2)
print('Set 2')
print()

#converts lists to sets and compares each list to see if there cross over numbers
print(set(li).intersection(set(li2)))
print('Numbers that match')
