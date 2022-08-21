
'''
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

'''

# Single line if else
print ("Number is positive " if int(input("Enter a number: "))>0 else "Number is Non positive")


x = input("Enter a number: ")
match x:
    case 1:
        print ("Hi")
    case 2:
        print("Hello")
        
