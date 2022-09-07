#Qustion 1
def fun1():
    print("MySirG")
fun1()

#Question 2
def fun2(a,b):
    print("Number is {} {} ".format(a,b))
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
fun2(num1, num2)

#Question 3
def fun3(*t):
    print(t)
fun3(10,20)
fun3(45, [34,56], "Hi")

#Question 4
def fun4(**kwargs):
    for key, value in kwargs.items():
        print("%s %s"%(key,value))
fun4(Good="Morning", Hello = "MySirG")

#Question5
def fun5(lst):
    for l in lst:
        print(l, end =' ')
fun5(["1",3.4, 5+6j, True])

#Question 6
def fun6(a,b,c,d):
    print(max(a,b,c,d))
fun6(1,78,45,34)

#Question 7
def fun7(lst):
    l=list()
    for i in lst:
        if type(i) not in (int,float):
            print("Enter only numbers in list!!")
            break
        else:
            l.append(i)
    print(sum(l))
fun7([1.6,2,6,3,4.6,5,6,7,8])

#Question 8
def fun8(lst):
    mult = 0
    for i in lst:
        if type(i) not in (int,float):
            print("Enter only numbers in list!!")
            break
        else:
            mult = mult+ i*i
    print(mult)
fun8([1.1,2,6,3,4,5,6,7,8,9,7])

#Question 9
def fun9(n):
    print(n in range(1,100))
fun9(10)
fun9(1000)

#Question 10
def fun10(n):
    print("True" if n%2 ==0 else "False")
fun10(77)
fun10(34)