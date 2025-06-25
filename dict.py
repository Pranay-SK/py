keys=[]
values=[]
print("for key:")
n=5
for i in range(0,n):
    element=int(input("Enter element"+str(i+1)+":"))
    keys.append(element)
    values.append(element*element)
    a=values
    
    
print("keys:",a)
d=dict(zip(keys,values))
print(d)