#1      The number is positive , negative,zero

num1 = int(input("Enter a number :"))
if num1>0:
    print("positive")
elif num1==0 :
    print("Zero")
else:
    print("negative")

# #2        even odd numbers

num2 = int(input("Enter a number :"))
if num2%2==0:
    print("even")
else:
    print("odd")

#3          eligible to vote or not

age = int(input("Enter your age :"))
if age>=0:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")


# #4          greatest of two numbers

num1 = int(input('enter first number :'))
num2  = int(input("enter second number :"))
if num1>num2:
    print("greatest number is ",num1)
elif num1 == num2:
     print("Both numbers are equal")
else:
    print("Greater number is ", num2)


# #5          studet marks > 40 then he is pass otherwise he is fail

marks = int(input("Enter Your marks"))
if marks>40:
    print("pass")
else:
    print("fail")

#using ternary operator 

marks = int(input("enter your marks :"))
result = "pass" if marks>40 else "fail"
print(result)

# #6            days of a week using switch case
# # import random
# # a  = random.randint(1,7)

day = int(input("enetr a number from 1 - 7 : "))
if day == 1 :
    print("Sunday")
elif day == 2:
    print("monday")
elif day == 3:
    print("tuesday")
elif day == 4:
    print("wednsday")
elif day == 5:
    print("thursday")
elif day == 6:
    print("friday")
elif day == 7:
    print("saturday")
else :
    print("please enetr only from 1 - 7 ")

#7                 simple calculations addition , multiplication , subtraction , division


def add(a,b):
    return a+b
def sub(a,b):
    return a - b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

print(add(10,20))
print(sub(20,30))
print(mul(20,4))
print(div(20,10))
print(mod(10,2))


#8             printing month name while given number 

month = int(input("Choose a number from 1 - 12 : "))
if month == 1 :
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("Aprail")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("Septembar")
elif month == 10:
    print("Octobar")
elif month == 11:
    print("Novembar")
elif month == 12:
    print("Decembar")
else :
    print("please Choose number only from 1 - 12 ")



#9             finding greatest of three numbers

a = input("Enter first number : ")
b = input("Enter second number : ")
c = input("Enter third number : ")

if a == b == c :
    print("The three numbers are equal")
else:
    if a>=b and a>=c :
        print("Greatest number is ",a)
    elif b>=a and b>=c:
        print("Greatest number is ",b)
    else:
        print("Greatest number is ",c)

#10           finding leap year 

year = int(input("Enter a year : "))

if  (year % 4 ==0 and year != 0) or year % 400 == 0 :
    print(year ,"is leap year ")
else:
    print(year , "is not a leap year ")

#11          consonents , ovwels , neither

check = input("Enter a character :").lower()

if len(check) == 1 :
    if check in ['a','e','i','o','u']:
        print("It is a ovwel")
    elif check not in ['a','e','i','o','u']:
        print("it is consonent ")
else:
    print("please enter single character only")

#12           printing Grade of students based on marks

marks = int(input("Enter Student Marks : "))

if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<=89:
    print("Grade B")
elif marks>=70 and marks<=79 :
    print("Grade C")
else:
    print("Fail")


#13       three sides lenghts can form a triangle

a = float(input("Enter first side length : "))
b = float(input("Enter second side length : "))
c = float(input("Enter third side length : "))

if a+b>c and b+c>a and a+c>b :
    print("Forms a triangle")
else:
    print("Does not form a triangle")





