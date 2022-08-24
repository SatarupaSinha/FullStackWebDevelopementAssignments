for i in range ((int(input("Enter a number: "))),1,-2):
    print(i, end =' ')
'''
str = input("Enter a String: ")
for s in str:
    if s =='r':
        break
    else:
        print(s, end ='')
else:
    print()
    print("All characters are printed")

str = input("Enter a String: ")
count = 0
for s in str:
    if s == 'a':
        count = count+1
print(count)


i = 1
while i<=3:
    x = int(input("Enter a number: "))
    if x%2 == 0:
        print("Winner !!")
        break
    i=i+1
else:
    print("You Lost!!")



i = 1
while i<=20:
    if i%2 ==0:
        print(i,end =' ')
    i=i+1


i = 10 
while i:
    print(i, end =' ')
    i=i-1

loop = 0
while loop <5:
    print("MySirG")
    loop=loop+1

x = int(input("Enter a number"))
if x > 0:
    print ("Number is positive ")
if x<0:
    print ("Number is Non positive ")
'''

'''
marks = int(input("Enter a marks: "))
if marks > 90 and marks <= 100:
    print("A")
elif marks > 80 and marks <=90:
    print("B")
elif marks > 70 and marks <=80:
    print("C")
elif marks > 60 and marks <=70:
    print("D")
elif marks >= 50 and marks <=60:
    print("E")
else:
    print("F")



# Single line if else
print ("Number is positive " if int(input("Enter a number: "))>0 else "Number is Non positive")


x = input("Enter a number: ")
match x:
    case 1:
        print ("Hi")
    case 2:
        print("Hello")
        
'''