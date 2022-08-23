#Answer 1

x = int(input("Enter a three digit number: "))
print(int(x/10))

#Answer 2
print(x%10)


#Answer 3
a = int(input("Enter a number: "))
b= int(input("Enter second number: "))
print (a, b)
a, b = b, a
print (a, b)

#Answer 4
c = int(input("Enter a number: "))
d= int(input("Enter second number: "))
print(pow(c,d))

#Write a python script which takes a three digit number from the user and displays only its first digit.
print(int(x/100))

#Write a python script which takes a three digit number from the user and displays only its middle digit.
print(int((x/10)%10))

#Write a python script which takes a three digit number from the user and displays only its last digit.
print(x%10)

#Write a python script to use IN operator to display the data present in the list
lst =[1,2,3,4,5,6,7]
print(2 in lst)

#Write a python script to use NOT IN operator to display the data not present in list
print(10 not in lst)

#Write a python script to use IS operator to display if both variables are the same object or not?
print (x is lst)