symbol=input()

if symbol.isalpha():
    print("IS ALPHA")
    if symbol.isupper():
        print("CAPITAL")
    else:
        print("SMALL")

else:
    print("IS DIGIT")
