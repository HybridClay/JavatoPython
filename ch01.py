#1.1
print("Welcome to Python")
print("Welcome to Computer Science")
print("Programming is fun\n")

#1.2
for i in range(1,6):
    print("Welcome to Java")

#1.3
print("")
print("pppppppppp        yyy   yyy   tttttttttttttt    h        h       ooooo       n          n     ")
print("p       ppppp     yyy   yyy        ttt          h        h      o     o      n n        n     ")
print("p       pppp      yyy   yyy        ttt          h        h     o       o     n   n      n     ")
print("ppppppppppp          yyy           ttt          hhhhhhhhhh     o       o     n     n    n     ")
print("p                    yyy           ttt          h        h     o       o     n       n  n     ")
print("p                    yyy           ttt          h        h      o     o      n        n n     ")
print("p                    yyy           ttt          h        h       ooooo       n          n     ")

#1.4
print("")
print("a     a^2     a^3")
for i in range(1,5):
    print(str(i) + "     " + str(i**2) + "     " + str(i**3))

#1.5
print("")
numerator = 9.5 * 4.5 - 2.5 * 3
denominator = 45.5 - 3.5
print(str(numerator/denominator))

#1.6
print("")
summation = 0
for i in range(1,10):
    summation += i
print(summation)

#1.7
print("")
a= 1.0
b= 1/3
c= 1/5
d= 1/7
e= 1/9
f= 1/11
g= 1/13
print(4*(a-b+c-d+e-f))
print(4*(a-b+c-d+e-f+g))

#1.8
print("Area and perimeter of a circle")
import math
radius = 5.5
perimeter = 2 * radius * math.pi
area = radius * radius * math.pi
print(perimeter)
print(area)

#1.9
print("Area and perimeter of a Rectangle")
width = 4.5
height = 7.9
print("area: " + str(width*height))
print("perimeter: " + str(width+width+height+height))

#1.10
print("")
mile = 1.6
kilometers = 14
minsec = 45.5
mph = (kilometers/mile)/(minsec/60)
print(mph)

#1.11
print("")

#1.12
OneMile = 1.6
MilesRun = 24
kph = (MilesRun*OneMile)/((60+40+(35/60))/60) #60 minutes in an 1hour plus 40 minutes plus 35sec/60minINHour divide all by 60min
print(kph)


