"""
#5.1
def getPentagonalNumber(n):
    return n*(3*n - 1)/2

count = 0
for i in range(1,101):
    num = getPentagonalNumber(i)
    count += 1
    if count % 10 == 0:
        print(str(int(num)))
    else:
        print(end= str(int(num)) + " ")
"""

"""
#5.2
def sumDigits(n):
    remainder = 0
    while int(n) != 0:
        remainder += int(n) % 10
        n = int(n) / 10
    return int(remainder)

num = input("Enter an integer: ")
print(str(sumDigits(int(num))))
"""

#5.3
def reverse(number):
    remainder = 0
    revNumber = 0
    while int(number) > 0:
        remainder = int(number) % 10
        number = int(number) / 10
        revNumber = int((revNumber * 10)) + int(remainder)
    return int(revNumber)

def isPalindrome(number):
    palindrome = int(number)
    reverse = 0

    while int(palindrome) != 0:
        remainder = int(palindrome) % 10
        reverse = int((reverse * 10)) + int(remainder)
        palindrome = int(palindrome) / 10

    return int(number) == int(reverse)

numb = input("Enter an integer: ")
print(reverse(int(numb)))
print(isPalindrome(int(numb)))
