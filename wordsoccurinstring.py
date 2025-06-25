def count_word(str1):
    str1=str1.split()
    str2=[]
    for i in str1:
        if i not in str2:
            str2.append(i)

    for i in str2:
        print("{} occurs {} times".format(i,str1.count(i)))

def main():
    str1="apple mao apple banana apple mango banana licchi mango"
    count_word(str1)

main()            