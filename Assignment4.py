#Write a python script to take your name as input from the user and then print it.
name = input("Enter your name: ")
print(name)

#Write a python script to take input from the user. Input must be a number.
number = int(input("Enter a number: "))
print(number)


#Write a python script which takes two numbers from the user, then calculate their sum and display the result.
number1 = int(input("Enter a number: "))
number2 = int(input("Enter second number: "))
print(number1 + number2)


#Write a python script which takes the radius from the user and display area of a circle.
import math as M
radius = float (input ("Enter the radius of the circle: "))
areaOfCircle = M.pi* radius * radius
print (areaOfCircle)


#Write a python script to calculate the square of a number. Number is entered by the user.
length = float (input ("Enter the length of the sqaure: "))
areaOfSquare = pow(length,2)
print (areaOfSquare)

#Write a python script to calculate the area of Triangle. Number is entered by the user.
height = float (input ("Enter the height of the sqaure: "))
breadth = float (input ("Enter the breadth of the sqaure: "))
areaOfTriangle = 1/2*height* breadth
print (areaOfTriangle)


#Write a python script to calculate average of three numbers, entered by the user
number = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))
avg = (number+number2+number3)/3
print(avg)


#Write a python script to calculate simple interest
principal = int(input("Enter a principal: "))
roi = float(input("Enter a Rate of Interest: "))
years = int(input("Enter a years: "))
si = (principal*roi*years)/100
print(si)


#Write a python script to calculate the volume of a cuboid.
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
vol = length*width*height
print(vol)


#Write a python script to calculate area of a rectangle
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
areOfRec = length*width
print(areOfRec)
