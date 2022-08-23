#Write a python script to check whether a given number is positive or non-positive
x = int(input("Enter a number: "))
print("Positive" if x>0 else "Non Positive")

#Write a python script to check whether a given number is divisible by 5 or not
x = int(input("Enter a number: "))
print("Divisble by 5" if x%5==0 else "Not divisble by 5")

#Write a python script to check whether a given number is even or odd
x = int(input("Enter a number: "))
print("Even" if x%2==0 else "Odd")

#Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
if x > y:
    print ("%d is greater" %x)
else:
    print ("%d is greater" %y)

#Write a python script to print two given words in dictionary order
x = input("Enter a word: ")
y = input("Enter another word: ")
if x> y:
    print (y, x)
else:
    print(x,y)

#Write a python script to check whether a given number is a three digit number or not.
i = 0
x = int(input("Enter a number: "))
while x%10 !=0:
    x = int(x/10)
    i=i+1
if i != 3:
    print("Not three digit Number")
else:
    print("Three digit Number")

#Write a python script to check whether a given number is positive, negative or zero.
x = int(input("Enter a number: "))
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")


#Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))
d = y * y - 4 * x * z 
if d> 0:
    print("Real & distinct roots")
elif d == 0:
    print("Real & equal roots")
else:
    print("Imaginary Roots")


#Write a python script to check whether a given year is a leap year or not.
x = int(input("Enter a year: "))
if (x%4==0 and x%100 !=0) or x%400==0:
    print("Leap Year")
else:
    print("Not a Leap Year")


#Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
x = int(input("Enter a number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x>y and x> z:
    print("%d is greatest " %x)
elif y>z:
    print("%d is greatest " %y)
elif z>y:
    print("%d is greatest " %z)


#Write a python script to take the month value in numeric format and display the number of days in it.
x = int(input("Enter a month in numeric: "))
if x ==2:
    print("28 days")
elif x == 4 or x ==6 or x ==9 or x ==11:
    print ("30 days ")
else:
    print("31 days")


#Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
x = complex(input("Enter a complex number: "))
if x.real > x.imag:
    print("Real part is greater")
else:
    print("Imaginary part is greater")