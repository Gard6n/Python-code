import sys

wind_speed = [5,10,15,20,25,30,35,40,45,50,55,60]

while True:
 
 temp = float(input('What is the temparature? '))
 degree = input('Fahrenheit or Celsius (F/C)? ')
 print('')
 if degree.upper() == 'F':
     for wind in wind_speed:
        #winds = wind

        wind_chill = 35.74 + 0.6215 * temp - 35.75 * 5**0.16 + 0.4275 * temp * 5**0.16
        wind_chill1 = 35.74 + 0.6215 * temp - 35.75 * 10**0.16 + 0.4275 * temp * 10**0.16
        wind_chill2 = 35.74 + 0.6215 * temp - 35.75 * 15**0.16 + 0.4275 * temp * 15**0.16
        wind_chill3 = 35.74 + 0.6215 * temp - 35.75 * 20**0.16 + 0.4275 * temp * 20**0.16
        wind_chill4 = 35.74 + 0.6215 * temp - 35.75 * 25**0.16 + 0.4275 * temp * 25**0.16
        wind_chill5 = 35.74 + 0.6215 * temp - 35.75 * 30**0.16 + 0.4275 * temp * 30**0.16
        wind_chill6 = 35.74 + 0.6215 * temp - 35.75 * 35**0.16 + 0.4275 * temp * 35**0.16
        wind_chill7 = 35.74 + 0.6215 * temp - 35.75 * 40**0.16 + 0.4275 * temp * 40**0.16
        wind_chill8 = 35.74 + 0.6215 * temp - 35.75 * 45**0.16 + 0.4275 * temp * 45**0.16
        wind_chill9 = 35.74 + 0.6215 * temp - 35.75 * 50**0.16 + 0.4275 * temp * 50**0.16
        wind_chill10 = 35.74 + 0.6215 * temp - 35.75 * 55**0.16 + 0.4275 * temp * 55**0.16
        wind_chill11 = 35.74 + 0.6215 * temp - 35.75 * 60**0.16 + 0.4275 * temp * 60**0.16
            

     print(f'At temperture: {temp}F, and wind speed: {5} mph, the windchill is: {wind_chill:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {10} mph, the windchill is: {wind_chill1:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {15} mph, the windchill is: {wind_chill2:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {20} mph, the windchill is: {wind_chill3:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {25} mph, the windchill is: {wind_chill4:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {30} mph, the windchill is: {wind_chill5:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {35} mph, the windchill is: {wind_chill6:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {40} mph, the windchill is: {wind_chill7:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {45} mph, the windchill is: {wind_chill8:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {50} mph, the windchill is: {wind_chill9:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {55} mph, the windchill is: {wind_chill10:.3}f')
     print(f'At temperture: {temp}f, and wind speed: {60} mph, the windchill is: {wind_chill11:.3}f')


     


 #if degree.lower() == 'c':