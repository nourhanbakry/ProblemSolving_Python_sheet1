numbers=input("enter 3 numbers: ")
x,y,z=map(int,numbers.split())
print(min(x,y,z),end=" ")
print(max(x,y,z))