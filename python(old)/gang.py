Child_price = float(input('Enter the price of an Childs meal: '))
print()
print('-----------------------------------------------------------------------------------------')
Adult_price = float(input('Little Piglet do you know the Price of an Adult '))
print()
print('-----------------------------------------------------------------------------------------')
Num_Child = int(input('How Many Children (MIDGETS)? '))
print()
print('-----------------------------------------------------------------------------------------')
Num_Adult = int(input('Adults? Do you know how many? '))
print()
print('-----------------------------------------------------------------------------------------')
saletax = float(input('Give me the rate that the government steals money from you? (Sale Tax) '))
print()
print('-----------------------------------------------------------------------------------------')
loser = float(input('How much did it cost you to be a loser? '))
print()
print('-----------------------------------------------------------------------------------------')
Fat = float(input('How Fat are you?(Lbs) '))
print()
print('-----------------------------------------------------------------------------------------')
#Everything Above ^^^^^ Is getting input from the user

Final_Price = float((Child_price*Num_Child)+(Adult_price*Num_Adult)+loser+Fat)
total = float(Final_Price+saletax)
#Adding up everything ^^^^^^^^^^^^

print()
print()
print()
#Making it look nice

print(f'Subtotal: ${Final_Price:.2f}')
print(f'Sale tax: ${saletax:.2f}')
print(f'Total: ${total:.2f}')
#Throwing up everything to the screen for the user to see

print()
print()
#Again More nice looking

payment = float(input('Enter Payment or die $'))
Change = total-payment
#More Math we be doing above ^^^^^^^^

if Change <= int('0'):
 print()
 print(f'Change ${Change:.2f}')
 end = input()
 #Prints How Much money that the Gets Back
else:
 print()
 print(f'You OWE ${Change:.2f}')
 end2 = input()
 #Prints How Much money that the user owes