"""
#3.1
import math

a, b, c = input("Enter a, b, c: ").split()

root = float(b)**2 - (4 * float(a) * float(c))

if root > 0:
    rootSquared = math.sqrt(root)
    r1 = (-float(b) + rootSquared) / (2*float(a))
    r2 = (-float(b) - rootSquared) / (2 * float(a))
    print("The roots are " + str(r1) + " " + str(r2))
elif root == 0:
    rootSquared = math.sqrt(root)
    r1 = (-float(b) + rootSquared) / (2 * float(a))
    print("The root is " + str(r1))
else:
    print("The equation has no real roots")
"""
import random

"""
#3.2
import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
num3 = random.randint(1,10)

answer = num1 + num2 + num3

user = input("Enter the sum of " + str(num1) + "+" + str(num2) + "+" + str(num3) + " ")

print(str(num1) + "+" + str(num2) + "+" + str(num3) + "=" + user + " " + str(bool(user==str(answer))))
"""

"""
#3.3
a, b, c, d, e, f = input("Enter a, b, c, d, e, f: ").split()
if float(a)*float(d) - float(b)*float(c) == 0:
    print("The equation has no solution")
else:
    x = (float(e)*float(d) - float(b)*float(f)) / (float(a)*float(d) - float(b)*float(c))
    y = (float(a)*float(f) - float(e)*float(c)) / (float(a)*float(d) - float(b)*float(c))
    print("x is " + str(x) + " and y is " + str(y))
"""

"""
#3.4
num1 = random.randint(1,100)
num2 = random.randint(1, 100)
user = input("Enter the sum of " + str(num1) + "+" + str(num2) + ": ")
answer = num1 + num2
if int(user) == int(answer):
    print("True, " + str(num1) + "+" + str(num2) + "=" + user)
else:
    print("False")
    print("The answer is: " + str(answer))
"""

"""
#3.5
today = input("Enter today's day: ")
elapsed = input("Enter the number of days elapsed since today: ")

if int(today) == 0:
    day = "Sunday"
elif int(today) == 1:
    day = "Monday"
elif int(today) == 2:
    day = "Tuesday"
elif int(today) == 3:
    day = "Wednesday"
elif int(today) == 4:
    day = "Thursday"
elif int(today) == 5:
    day = "Friday"
elif int(today) == 6:
    day = "Saturday"

futureDay = int(today) + int(elapsed)
if int(futureDay) > 6:
    futureDay %= 7

if int(futureDay) == 0:
    date = "Sunday"
elif int(futureDay) == 1:
    date = "Monday"
elif int(futureDay) == 2:
    date = "Tuesday"
elif int(futureDay) == 3:
    date = "Wednesday"
elif int(futureDay) == 4:
    date = "Thursday"
elif int(futureDay) == 5:
    date = "Friday"
elif int(futureDay) == 6:
    date = "Saturday"

print("Today is " + day + " and the future day is " + date)
"""

"""
#3.6
pounds = input("Enter weight in pounds: ")
feet = input("Enter feet: ")
inches = input("Enter inches: ")

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254
weightInKilograms = float(pounds) * KILOGRAMS_PER_POUND
height = (float(feet) * 12) + float(inches)
heightInMeters = height * METERS_PER_INCH
BMI = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is " + str(BMI))

if BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")
"""

#3.7

"""
#3.8
num1, num2, num3 = input("Enter three integers: ").split()

temp = 0
if int(num2) < int(num1) or int(num3) < int(num1):
    if int(num2) < int(num1):
        temp = num1
        num1 = num2
        num2 = temp

    if int(num3) < int(num1):
        temp = num1
        num1 = num3
        num3 = temp


if int(num3) < int(num2):
    temp = num2
    num2 = num3
    num3 = temp

print(num1 + " " + num2 + " " + num3)
"""

"""
#3.9
isbn = input("Enter the first 9 digits of an ISBN as integer: ")

d1 = int(isbn) / 100000000
remainingDigit = int(isbn) % 100000000
d2 = int(isbn) / 10000000
remainingDigit %= 10000000
d3 = int(remainingDigit) / 1000000
remainingDigit %= 1000000
d4 = int(remainingDigit) / 100000
remainingDigit %= 100000
d5 = int(remainingDigit) / 10000
remainingDigit %= 10000
d6 = int(remainingDigit) / 1000
remainingDigit %= 1000
d7 = int(remainingDigit) / 100
remainingDigit %= 100
d8 = int(remainingDigit) / 10
remainingDigit %= 10
d9 = int(remainingDigit)

d10 = (int(d1) + int(d2) * 2 + int(d3) * 3 + int(d4) * 4 + int(d5) * 5 + int(d6) * 6 + int(d7) * 7 + int(d8) * 8 + int(d9) * 9) % 11

if int(d10) == 10:
    print(str(d10))
    print("The ISBN-10 number is " + str(isbn) + "X")
else:
    print("The ISBN-10 number is " + str(isbn) + str(round(d10)))
"""

"""
#3.10
num1 = random.randint(1,100)
num2 = random.randint(1,100)
user = input("What is " + str(num1) + "+" + str(num2) + "? ")
answer = num1 + num2
if int(num1) + int(num2) == int(user):
    print("You are correct!")
else:
    print("You answer is wrong")
    print(str(num1) + "+" + str(num2) + " is " + str(answer))
"""

#3.11

"""
#3.12
num = input("Enter an integer: ")
if int(num) % 5 == 0 and int(num) % 6 == 0:
    print(str(num) + " is divisible by both 5 and 6")
elif int(num) % 5 == 0 or int(num) % 6 == 0:
    print(str(num) + " is divisible by 5 or 6, but not both")
else:
    print(str(num) + " is not divisible by either 5 or 6")
"""

#3.13

"""
#3.14
choice = input("Enter 0 for heads or 1 for tails: ")
coin = random.randrange(0,2) #NOTE: 0 included and 2 excluded
if int(choice) == int(coin):
    print("Coin flip was: " + str(coin))
    print("Your guess was " + str(choice))
    print("Your guess is correct!")

else:
    print("Coin flip was: " + str(coin))
    print("Your guess was " + str(choice))
    print("Your guess is incorrect :( ")
"""

#3.15

"""
#3.16
letters = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z']

randomIndex = random.randrange(0,26)
print(letters[randomIndex].upper())
"""

#3.17
choice = input("scissor (0), rock (1), paper(2): ")
rps = random.randint(0,2) #NOTE:Both inclusive

if int(rps) == 0 and int(choice) == 2:
    print("The computer is scissor. You are paper.")
    print("The computer won")
elif int(rps) == 0 and int(choice) == 1:
    print("The computer is scissor. You are rock.")
    print("YOU WON!")
elif int(rps) == 1 and int(choice) == 0:
    print("The computer is rock. You are scissor.")
    print("The computer won")
elif int(rps) == 1 and int(choice) == 2:
    print("The computer is rock. You are paper.")
    print("YOU WON!")
elif int(rps) == 2 and int(choice) == 0:
    print("The computer is paper. You are scissor.")
    print("YOU WON!")
elif int(rps) == 2 and int(choice) == 1:
    print("The computer is paper. You are rock")
    print("The computer won")
elif int(rps) == 0 and int(choice) == 0:
    print("The computer is scissor. You are scissor too. It is a draw")
elif int(rps) == 1 and int(choice) == 1:
    print("The computer is rock. You are rock too. It is a draw")
elif int(rps) == 2 and int(choice) == 2:
    print("The computer is paper. You are paper too. It is a draw")
else:
    print(str(rps) + " is not one of the choices")

