num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
if num1 == num2 == 0:
    print("Since both numbers are 0 the GCD cannot be defined")
elif num1 == 0 or num2 == 0:
    print("The GCD of the two given numbers",
          num1, "&", num2, "is", max(abs(num1), abs(num2)))
else:
    temp1 = abs(num1)
    temp2 = abs(num2)
    dividend = max(temp1, temp2)
    divisor = min(temp1, temp2)
    remainder = 1
    while remainder != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder
    print("The GCD of the two given numbers",
          num1, "&", num2, "is", dividend)
