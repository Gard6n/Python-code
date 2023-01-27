
def binaryS(list, target):

    first = 0
    last = len(list) - 1

    while first <= last:

        midpoint = (first + last)//2

    if list[midpoint] == target:

        return midpoint

    elif list[midpoint] < target:

        first = midpoint + 1


da = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

