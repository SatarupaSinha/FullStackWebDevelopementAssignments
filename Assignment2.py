#Answer 1
print("Learning Python")


'''Answer2
This will print value of 4 variables '''
a, b, c ,d = True, 3.4, 5, "This is a string"
print(a,b,c,d, sep ="\n")



#Answer 3
a,b,c,d, e= 5, True, 3.45, "MySirG", 3+4j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#Answer 4
number1 = 345
number2 = 345
print(id(number1))
print(id(number2))

#Answer 5
a,b,c,d= 5, True, 3.45, "MySirG"
print(a, type(a), id(a))
print(b, type(b), id(b))
print(c, type(c), id(c))
print(d, type(d), id(d))


#Answer 6
from keyword import kwlist
print (kwlist)

#Answer 7
#help() -> keywords

#Answer 8
#from A1 import x
#print(x)

#Answer 9
#True, False, None

#Answer 10
# Python Program to Get Current Date and Time
from datetime import datetime
today = datetime.now()
dt = today.strftime("%d-%m-%Y and %I PM")
print("Current Date and Time = ", dt)
