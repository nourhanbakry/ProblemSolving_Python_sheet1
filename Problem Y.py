numbers=input("enter 4 numbers: ")
x,y,z,l=map(int,numbers.split())
product=x*y*z*l
print(product%100)