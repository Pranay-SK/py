def count(s,sub):
    c=s.count(sub)
    if c:
        print(f"yes,'{sub}' found {c} times")

    else:
        print("does not found")

main="a geek in need is a geek indeed"
sub="geek"
count(main,sub)