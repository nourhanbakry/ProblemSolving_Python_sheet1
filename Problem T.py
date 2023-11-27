numbers=input("enter three numbers: ")
x,y,z=map(int,numbers.split())
list=[x,y,z]
asending=sorted(list)

for n in asending:
       print(n)
       
print()

for i in list:
       print(i)
