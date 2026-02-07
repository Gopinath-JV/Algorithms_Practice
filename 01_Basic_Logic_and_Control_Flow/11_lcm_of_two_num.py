num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
if num1 == 0 or num2 == 0:
    print("LCM of the numbers is 0")
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
    lcm = (temp1*temp2) // dividend
    print("the LCM of the given two numbers", num1, "&", num2, "is", lcm)
