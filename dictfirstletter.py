def convert(list):
    dict={list[i]:list[i+1] for i in range(0,len(list),2)}
    return dict
list1=['a','adi','b','bhavik','d','darshan']
print("dictionary is:",convert(list1))