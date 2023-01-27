
from distutils.archive_util import make_archive


#Start of a class
class car:
#allows objects to have attributtes to them
    def __init__(self,make,year,color):

         self.make = make
         self.year = year
         self.color = color


    def driving(self):
        print('This car is currently driving')
        
#Adding the class method to a object attributte
    def stop(self):
        print('This '+self.make+' is currently stopped')

#calling a object with the class car and defining the attributes
woo = car('toyoda','1993','blue')
dra = car('gogonut',"2200",'deep black')

print()
print()
print(f'the make of the car is {woo.make} and the other make is {dra.make}')
print()
print()
print(woo.stop())