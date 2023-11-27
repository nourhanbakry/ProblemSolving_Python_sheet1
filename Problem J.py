numbers=input("enter your numbers: ")
x,y=map(int,numbers.split())
if x>y or x==y:
    if x%y==0:
        print("Multipliers")
    else:
       print(" Not Multipliers") 
else:
    if y%x==0:
       print("Multipliers")
    else:
         print(" Not Multipliers") 

 