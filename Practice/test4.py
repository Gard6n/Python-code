
inputnumber = int(input())
countnumber = inputnumber
digitcount = 0
while countnumber > 0:
    digitcount += 1
    countnumber = countnumber//10

print(digitcount) 