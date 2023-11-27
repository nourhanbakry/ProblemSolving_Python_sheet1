n=float(input("enter a number: "))
if n>=0 and n<=25:
    print("interval [0,25]")
elif n>25  and n<=50:
    print("interval (25,50]")
elif n>50 and n<=75:
    print("interval (50,75]")
elif n>75 and n<=100:
    print("interval (75,100]")
else:
    print("Out of the intervals")