import math
radius = eval(input('Enter a value for radius:'))

Area = math.pi*(radius**2)
if radius > 0:
    print('The Area of your circle is:', Area)
else: print('Incorrect input!')
