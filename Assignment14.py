
#Answer 1
n = int(input("Enter the number of natural number: "))
l1 = [x for x in range(1, n+1)]
print(l1)

#Answer 2
n = int(input("Enter the number of natural number: "))
l1 = [x for x in range(1, n+1,2)]
print(l1)

#Answer 3
n = int(input("Enter the number of natural number: "))
l1 = [x for x in range(2, n+1, 2)]
print(l1)

#Answer 4
print(max(l1))

#Answer 5
print(min(l1))

#Answer 6
print(sum(l1))


#Answer 7
l2 = ["A",4.5,3,4,5,6,7,20, 3455,673,True,False,"Python","Cpp", 4+6j]
print(l2)
i =0
l3 = list()
while i<len(l2):
    if type(l2[i]) == int:
        l3.append(l2[i])
    else:
        pass
    i=i+1
print(l3)

#Answer 8
test_list = [1,2,3,4,5,6,7,7,2,3,4,2,3,23,4,5,79,90,4,2,56,7,8,9,9,98,6]
d = {}
for x in test_list:
    d[x] = d.get(x,0) + 1
print(f"The original list : {test_list}" )
print(f"The list frequency of elements is : {d}" )4

#Answer 9
test_list = [1,2,3,4,5,6,7,7,2,3,4,2,3,23,4,5,79,90,4,2,56,7,8,9,9,98,6]
number = int(input("Enter a number : "))
print(test_list.index(number)+1)

#Answer 10
test_list = [1,2,3,4,5,6,7,7,2,3,4,2,3,23,4,5,79,90,4,2,56,7,8,9,9,98,6]
print(sorted(test_list))
