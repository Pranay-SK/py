l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
l2=[3,4,7,8,99,9,11,13,1,109,66,2]
l3=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if(l1[i]==l2[j]):
            l3.append(l1[i])
print("Intersection of the two lists is:",l3)