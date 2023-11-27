numbers=input("enter two numbers: ")
x,y=map(int,numbers.split())
if x>y or x==y:
    print("Yes")
else:
    print("No")