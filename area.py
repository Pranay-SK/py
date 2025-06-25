A=int(input("Enter the number between 1 to 3 ,,1.circle 2.rectangle 3.triangle:"))

if A==1:
    r=int(input("Enter the radius of circle:"))
    area1=3.14*r*r
    print("Area of circle is:", area1)

elif A==2:
    l=int(input("Enter the length:"))
    b=int(input("Enter the breadth:"))
    area2=l*b
    print("Area of rectangle is:",area2)
else:
    b=int(input("Enter the base:"))
    h=int(input("Enter the height:"))
    area3=1/2*b*h
    print("Area of triangle is:",area3)
    