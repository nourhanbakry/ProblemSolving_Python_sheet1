numbers=input("enter 4 numbers: ")
a,b,c,d=map(int,numbers.split())
if a**b>c**d:
    print("YES")
else:
    print("NO")