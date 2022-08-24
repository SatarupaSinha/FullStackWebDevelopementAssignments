#Answer 1
x = int(input("Enter the number of times you wish to print: "))
for i in range (1,x+1):
    print("MySirG")

#Answer 2
x = int(input("Enter the number: "))
for i in range (1,x+1):
    print(i, end=' ')
print()

#Answer 3
x = int(input("Enter the number: "))
for i in range (x,0,-1):
    print(i, end =' ')
print()

#Answer 4
x = int(input("Enter the number: "))
for i in range (1,x+1,2):
    print(i, end=' ')
print()

#Answer 5
x = int(input("Enter the number: "))
if x%2==0:
    for i in range (x-1,0,-2):
        print(i, end=' ')
else:
    for i in range (x,0,-2):
        print(i, end=' ')
print()

#Answer 6
x = int(input("Enter the number: "))
for i in range (2,x+1,2):
        print(i, end=' ')
print()

#Answer 7
x = int(input("Enter the number: "))
if x%2==0:
    for i in range (x,0,-2):
        print(i, end=' ')
else:
    for i in range (x-1,0,-2):
        print(i, end=' ')
print()


#Answer 8
x = int(input("Enter the number: "))
for i in range (1,x+1):
    print(pow(i,2), end=' ')
print()


#Answer 9
x = int(input("Enter the number: "))
for i in range (1,x+1):
    print(pow(i,3), end=' ')
print()

#Answer 10
x = int(input("Enter the number: "))
for i in range (1,x+1):
    print(i*10, end=' ')
print()