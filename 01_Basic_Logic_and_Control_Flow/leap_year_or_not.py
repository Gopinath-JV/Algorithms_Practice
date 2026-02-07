year = (int(input("Enter the year:")))
if year <= 0:
    print("the entered year", year, "is invalid")
elif (year % 400 == 0):
    print("The entered year", year, "is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("The entered year", year, "is a leap year")
else:
    print("the entered year", year, "is not a leap year")
