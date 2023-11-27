import math
numbers=input("enter two numbers: ")
x,y=map(int,numbers.split())
floor=x//y
ceil=math.ceil(x/y)
round=round(x/y)   #الراوند تعبانه تقريبا مش راضيه تشتغل
print(f"floor {x} / {y} = {floor}")
print(f"ceil {x} / {y} = {ceil}")
print(f"round {x} / {y} = {round}")


