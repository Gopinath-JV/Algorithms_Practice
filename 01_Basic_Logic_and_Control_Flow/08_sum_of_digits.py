num = int(input("Enter any number: "))
temp = abs(num)
sum_of_digits = 0
while temp > 0:
    sum_of_digits = sum_of_digits + (temp % 10)
    temp = temp//10
print("sum of the digits for the given number", num, "is", sum_of_digits)
