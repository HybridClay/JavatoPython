"""
#4.1
countPos = 0
countNeg = 0
total = 0
avg = 0
num =input("Enter an integer, the input ends if it is 0: ")

if num == 0:
    print("No numbers are entered except 0")

while int(num) != 0:
    if int(num) > 0:
        countPos += 1
    elif int(num) < 0:
        countNeg += 1

    total += int(num)
    avg = int(total) / (countPos + countNeg)
    num = input("Enter an integer, the input ends if it is 0: ")

print("The number of positives is " + str(countPos))
print("The number of negatives is " + str(countNeg))
print("The total is " + str(total))
print("The average is " + str(avg))
"""

"""
#4.2
import random
NUMBER_OF_QUESTIONS = 10
correctCount = 0
count = 0
output = ""

while count < NUMBER_OF_QUESTIONS:
    num1 = random.randint(1,15)
    num2 = random.randint(1,15)

    answer = input("What is " + str(num1) + "+" + str(num2) + "? ")

    if num1 + num2 == int(answer):
        print("You are correct!")
        correctCount+=1
    else:
        print("Your answer is wrong \n" + str(num1) + "+" + str(num2) + " should be " + str(num1+num2))

    count+=1
    output += "\n" + str(num1) + "+" +str(num2) + "=" + str(answer) +   {True:" correct", False:" wrong"} [int(num1) + int(num2) == int(answer)]

print("Correct count is " + str(correctCount) + "\nTest results " + output)
"""

"""
#4.3
print("Kilograms     Pounds")
for i in range(1,200):
    print(str(i) + "\t\t\t   %.1f"  % (i*2.2))
"""

"""
#4.4
print("Miles     Kilograms")
for i in range(1,200):
    print(str(i) + "\t\t   %.3f"  % (i*1.609))
"""

"""
#4.5
print("Kilograms\t Pounds   | \tPounds\t\t Kilograms")
for k, p in zip(range(1,200,2), range(20,516,5)):
    pounds = k * 2.2
    kilograms = p / 2.2
    print(str(k) + "\t\t\t   %.1f" % pounds + "   |\t   " + str(p) + "\t\t%.2f" % kilograms)
"""

"""
#4.6
print("Miles\t Kilometers   | \tKilometers\t\t Miles")
for m, k in zip(range(1,11), range(20,70,5)):
    kilometers = m * 1.609
    miles = k / 1.609
    print(str(m) + "\t\t\t   %.3f" % kilometers + "   |\t   " + str(k) + "\t\t%.3f" % miles)
"""


#4.7
TUITION = 100000
increasePercent = 0.05
newTuition = 0

for i in range(1,11):
    tuitionincrease = TUITION * increasePercent
    TUITION = TUITION + tuitionincrease
    print("Tuition increase in year " + str(i) + " is: " + str(tuitionincrease))
    print("Tuition is now: " + str(TUITION))


totalCost = 0;
for year in range(1,5):
    print("Tuition for year " + str(year) + " is: ")
    universityinc = TUITION * increasePercent
    TUITION = TUITION + universityinc
    print(TUITION)
    totalCost += TUITION

print("The total cost of four years' worth of tuition starting ten years from now is: ${:,.2f}".format(round(totalCost)))


