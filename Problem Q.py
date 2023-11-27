numbers=input("enter 2 numbers: ")
x,y=map(float,numbers.split())

if x==0 and y==0:
    print("origan point")
elif x<0 and y>0:
    print("Q2")
elif x<0 and y<0:
    print("Q3")
elif x>0 and y>0:
    print("Q1")
elif x>0 and y<0:
    print("Q4")
else:
    print("ON the axis")
