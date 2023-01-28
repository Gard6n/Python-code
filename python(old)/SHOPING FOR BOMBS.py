import sys

# Main Variables
items = []
Prices = []
# Main Variables

# Sub Variables
i = None
total_amount = 0
# Sub Variables

#Starts the loop for the program
loop_start = 1
while loop_start == 1:

 # Menu 
 print()
 print('DA SHOPING CART OF DEATH!!')
 print()
 print('Please select one of the following options')
 print('----------------------------------')
 print('1: Add Item')
 print('2: View Cart')
 print('3: Remove Item')
 print('4: Compute total')
 print('5: Get Called Stupid')
 print('6: Quit')
 # Menu 

 print('-------------------------------')
 user = input('Enter Something Stupid ')
 print('-------------------------------')

 # If the user enters the 1st option 
 if user.lower() == 'add item':

  print()
  print('-------------------------------')
  print('What item would you like to add?')
  print('-------------------------------')
  item = input()
  items.append(item)
  
  print()
  print('---------------------------')
  print(f'What is the price of {item}?')
  print('---------------------------')
  item_price = float (input())
  Prices.append(item_price)

  print()
  print('----------------------------')
  print(f'{item} was added to the cart!')
  print('----------------------------')
  print()

 #If the user enters the 2nd option
 if user.lower() == 'view cart':

     for i in range(len(items)): 
        items1 = items[i]
        Price = Prices[i]
        print()
        print('----------------------')
        print(f'{i+1}.{items1} - ${Price:.2f}')
        print('----------------------')

     if i == None:
        print() 
        print("-------------")
        print('Cart Empty!')
        print("-------------")

#If the user enters the 3rd option
 if user.lower() == 'remove item':
    print('What item would you like to remove?')

    num = int(input())
    num -= 1
    if num > i:
        print('Thats a invaild number')
        num = int(input('Enter a new number '))
        num -= 1
    items.pop(num)
    Prices.pop(num)
    print()
    print('-----------')
    print('Item Removed!')
    print('-----------')

#If the user enters the 4th option
 if user.lower() == 'compute total':
     
     for total in Prices:
         total_amount += total
         
     print(f'The price of the items in the shopping cart is ${total_amount:.2f}')

# if the user enters the 5th option
 if user.lower() == 'get called stupid':
     print()
     print('----------------------------------')
     print('YOUR SOOOOOOO DUMB!! AND STUPID!!!')
     print('----------------------------------')


 # Makes the program DIEEEE!!
 if user.lower() == 'quit':
    sys.exit()




