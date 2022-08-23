#Answer 1
x = int(input("Enter a month in numeric: "))
match x:
    case 2:
        print("28 days")
    case 4:
        print("30 days")
    case 6:
        print("30 days")
    case 9:
        print("30 days")
    case 11:
        print("30 days")
    case _:
        print("31 days")

#Answer 2
x = int(input("Enter a number: "))
y = int(input("Enter second number: "))
choice = (input("Enter 1 for addition , 2 for substraction, 3 for multiplication and 4 for division"))
match choice:
    case "1":
        print(x+y)
    case "2":
        print(x-y)
    case "3":
        print(x*y)
    case "4":
        print(x/y)

#Answer 3
x = int(input("Enter a side of triangle: "))
y = int(input("Enter second side of triangle: "))
z = int(input("Enter third side of triangle: "))
choice = (input("Select 1/2/3/4"))
match choice:
                case "3":
                    if x == y == z:
                        print("Equilateral Triangle")
                    else:
                       print("Not Equilateral Triangle")
                case "1":
                    if x == y or y == z or z == x:
                        print("Isosceles Triangle")
                    else:
                       print("Not Isosceles Triangle")
                case "2":
                    print ("Right angle Triangle")



