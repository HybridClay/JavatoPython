"""
#2.1
celsius = input("Enter a degree in Celsius: ")
fahrenheit = (9/5) * float(celsius) + 32
print(str(celsius) +" Celsius is " + str(fahrenheit) + " Fahrenheit")
"""
import math

"""
#2.2
import math
radius, length = input("Enter the radius and length of a cylinder: ").split()
area = float(radius) * float(radius) * math.pi
volume = area * float(length)
print("The are is " + str(area))
print("The volume is " + str(volume))
"""

"""
#2.3
feet = input("Enter a value for feet: ")
meters = float(feet) * 0.305
print(str(feet) + " feet is " + str(meters) + " meters")
"""

"""
#2.4
pounds = input("Enter a number in pounds: ")
kilograms = float(pounds) * 0.454
print(str(pounds) + " pounds is " + str(kilograms) + " kilograms")
"""

"""
#2.5
subtotal, gratuity_rate = input("Enter the subtotal and gratuity rate: ").split()
gratuity = (float(subtotal) * float(gratuity_rate))/100
total = float(subtotal) + gratuity
print("The gratuity is $" + str(gratuity) + " and total is $" + str(total))
"""

"""
#2.6
summ = 0
remainder = 0
number = input("Enter a number between 0 and 1000: ")
while int(number) > 0:
    remainder = int(number) % 10
    summ += remainder
    number = int(number) / 10
print("The sum of the digits is " + str(summ))
"""

"""
#2.7
minutes = input("Enter the number of minutes: ")
hours = int(minutes)/60
days = int(hours)/24
years = int(days)/365
daysleft = int(days) % 365
print(str(minutes) + " minutes is approximately " + str(int(years)) + " years and " + str(daysleft) + " days" )
"""

#2.8

"""
#2.9
v0, v1, t = input("Enter v0, v1, and t: ").split()
acceleration = (float(v1) - float(v0)) / float(t)
print("The average acceleration is " + str(acceleration))
"""

"""
#2.10
water = input("Enter the amount of water in kilograms: ")
temperature = input("Enter the initial temperature: ")
finalTemp = input("Enter the final temperature: ")
energy = float(water) * (float(finalTemp) - float(temperature)) * 4184
print("The energy needed is: " + str(energy))
"""

#2.11

"""
#2.12
speed, acceleration = input("Enter speed and acceleration: ").split()
runwayLength = (float(speed)**2) / (2*float(acceleration))
print("The minimum runway length for this airplane is " + str(runwayLength))
"""

"""
#2.13
savings = input("Enter the monthly savings amount: ")
value = 0
value = float(savings) * (1 + 0.00417)
value = (float(savings) + float(value)) * (1+0.00417)
value = (float(savings) + float(value)) * (1+0.00417)
value = (float(savings) + float(value)) * (1+0.00417)
value = (float(savings) + float(value)) * (1+0.00417)
value = (float(savings) + float(value)) * (1+0.00417)
print("After the sixth month, the account value is $%.2f" %value)
"""

"""
#2.14
pounds = input("Enter weight in pounds: ")
height = input("Enter height in inches: ")
BMI = (float(pounds)*0.45359237) / (float(height)*0.0254)**2
print("BMI is " + str(BMI))
"""

"""
#2.15
x1, y1, x2, y2, x3, y3 = input("Enter three points for a triangle: ").split()

sidex1 = float(x2) - float(x1)
sidey1 = float(y2) - float(y1)

sidex2 = (float(x3) - float(x2))
sidey2 = float(y3) - float(y2)

sidex3 = float(x1) - float(x3)
sidey3 = float(y1) - float(y3)

side1 = math.sqrt(sidex1**2 + sidey1**2)
side2 = math.sqrt(sidex2**2 + sidey2**2)
side3 = math.sqrt(sidex3**2 + sidey3**2)

s = (side1 + side2 + side3) / 2
area = math.sqrt(float(s) * (float(s) - side1) * (float(s) - side1) * (float(s) - side1))

print("The area of the triangle is " + str(round(area,2)))
"""

""""
#2.16
side = input("Enter the side: ")
area = ((3*math.sqrt(3)) / 2) * (float(side)**2)
print("The area of the hexagon is " + str(area))
"""

"""
#2.17
temperature = input("Enter the temperature in Fahrenheit: ")
v = input("Enter the wind speed in miles per hour: ")
WCI = 35.74 + (0.6215*float(temperature)) - 35.75 * float(v)**0.16 + 0.4275*float(temperature)*float(v)**0.16
print("The wind chill index is " + str(WCI))
"""

"""
#2.18
print("a     b     pow(a,b)")
for i in range(1,6):
    print(str(i) + "     " + str(i+1) + "     " + str(i**(i+1)))
"""

"""
#2.19
x1, y1 = input("Enter x1 and y1: ").split()
x2, y2 = input("Enter x2 and y2: ").split()
distance = math.sqrt( ((float(x2) - float(x1))**2) + ((float(y2) - float(y1))**2) )
print("The distance between the two points is " + str(distance))
"""

"""
#2.20
balance, interestRate = input("Enter balance and interest rate (e.g., 3 for 3%): ").split()
interest = float(balance) * (float(interestRate)/1200)
print("The interest is " + str(interest))
"""


#2.21
investmentAmount = input("Enter investment amount: ")
interestRate = input("Enter annual interest rate in percentage: ")
interestRate = float(interestRate) / 1200
years = input("Enter number of years: ")
value = int(investmentAmount) * (1 + float(interestRate))**(float(years)*12)
print("Accumulated value is $" + str(value))

