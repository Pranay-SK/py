def recu(lst):
    if not lst:
        return 0
    return 1+recu(lst[1:])

mylist=[1,2,3,4,5,6,7,8]
print("length is:",recu(mylist))