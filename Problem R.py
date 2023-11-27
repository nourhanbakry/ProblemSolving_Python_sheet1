age=int(input("enter your days of age: "))
years=age//365
months=(age%365)//30
days=(age%365)%30

print(years, "years")
print(months, "months")
print(days, "Days")