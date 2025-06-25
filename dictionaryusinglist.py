dict1={}
l1=['a','b','c','d']
l2=['darshan','jayesh','lalit','madhur']
for i in range(len(l1)):
    dict1[l1[i]]=l2[i]

print("Dictionary is:",dict1)    

print("\n")
print("\n")
def find(list):

    dict2={list[i]:list[i+1] for i in range(0,len(list),2)}

    return dict2
list1=['a','madhur','b','jayesh','c','lalit','d','darshan']
print("dictionary is:",find(list1))