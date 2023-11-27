intervals=input("enter two intervals: ")
x,y,z,l=map(int,intervals.split())
if y>z and l>x:
    if y>x and l>z:
        print(z, y)
    else:
        print("erorr")
elif y<z and l>x:
    if y>x and l>z:
        print("-1")
    else:
        print("erorr")
else:
    print("invalid")