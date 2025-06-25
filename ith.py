def delith(lst,word,i):
    c=0
    for j in range(len(lst)):
        if lst[j]==word:
            c+=1
            if c==i:
                del lst[j]
                break
    return lst

w=['apple','banana','apple','cherry','apple','mango']
print(w)
print(delith(w,'apple',3))
print("\n")
print("\n")
print("\n")
def even(lst,w):
    c=0
    res=[]
    for j in lst:
        if j==w:
            c+=1
            if c%2==0:
                continue
        res.append(j)
    return res
a=['apple','banana','apple','apple','banana','apple','apple']
print(a)
print("Modified:",even(a,'apple'))