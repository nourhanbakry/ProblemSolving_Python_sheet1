operation=input("enter your operation sepated by distance: ").split()
n1=int(operation[0])
sign=operation[1]
n2=int(operation[2])

if sign==">":
    if n1>n2:
        print("Right")
    else:
        print("Wrong")

elif sign=="<":
    if n1<n2:
        print("Right")
    else:
        print("Wrong")

elif sign=="=":
    if n1==n2:
        print("Right")
    else:
        print("Wrong")

else:
    print("enter a valid sign")
