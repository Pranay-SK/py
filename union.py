import itertools
l1=[]
num1=int(input("Enter size of list1:"))
for i in range(num1):
    number1=int(input("Enter the numbers:"))
    l1.append(number1)

l2=[]
num2=int(input("Enter size of list2:"))
for i in range(num2):
    number2=int(input("Enter the numbers:"))
    l2.append(number2)

union=list(set().union(l1,l2))
print("Union of the two lists is:",union)

o=l1+l2
print("The concat lists is:",o)

l1.extend(l2)
print(l1)

lists=list(itertools.chain(l1,l2))
print(lists)

multiply=[l1*l2 for l1,l2 in zip(l1,l2)]
print(multiply)