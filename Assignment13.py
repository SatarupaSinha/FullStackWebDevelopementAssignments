#Answer 1
l1 = ["Java", "Python", "SQL", "C"]
print(l1)

#Answer 2
print(type(l1))
for x in l1:
    print(type(x))

#Answer 3
l2 = ["Java", "C" ,"Python"]
print(l2[-1])

#Answer 4
l3 = ["Java","SQL", "C", "Reactnative", "Javascript", "Python"]
i =0
for x in l3:
    if x == "Reactnative":
        l3[i] = "Flutter"
        i+=1
    elif x == "SQL":
        l3[i] = "NoSQL"
        i+=1
    else:
        i+=1
print(l3)

#Answer 5
l4 = ["Java","SQL", "C", "Reactnative"]
l4.append("Python")
print(l4)

#Answer 6
l5 = ["Java", "Python", "SQL"]
l6 = ["C", "Cpp", "NoSQL"]
print(l5+l6)

#Answer 7
l3 = ["Java","SQL", "C", "Reactnative", "Javascript", "Python"]
i =0
for x in l3:
    print(l3[i], end = "  ")
    i+=1
print()

#Answer 8
print(sorted(l3))

#Answer 9
n = eval(input("Enter the number of cities: "))
i = 0
l7 = list()
while i<n:
    city = input("Enter the name of the city: ")
    l7.append(city)
    i=i+1
print(l7)

#Answer 10
n = eval(input("Enter the number of enteries: "))
i = 0
l8 = list()
while i<n:
    number = int(input("Enter a two digit number: "))
    if number > 9:
        k = int(number %10)
        l = int(number/ 10)
        l8.append(str(l))
        l8.append(str(k))
    else:
        l8.append(str(number))
    i=i+1
print(l8)