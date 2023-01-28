import sys 
import csv

# Sub Variables
one_up = None
name = -3



while True:
    # User Input
    yes = input('If you want to continue enter YES, if not enter KILL ')

    # Main Program 
    if yes.lower() == 'yes':

        #Year = int(input('Enter the year of interest: '))
    
        with open('life.csv') as life:
            some = []
            total_dates = 0
            for line in life:
                dirty = line.strip()
                clean_life = dirty.split(',')
                print(clean_life[2])
                total_dates += clean_life[2]
                some.append(clean_life)

                for New in clean_life:
                    one_up = New

                # if New > one_up:

                    #Sprint(f'The overall max life expectancy is: {some}')

    if yes.lower() == 'kill':
        sys.exit()           