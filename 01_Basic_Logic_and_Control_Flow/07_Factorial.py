num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print("The factorial of", num, "is 1.")
else:
    factorial = 1
    while num > 1:
        factorial = factorial * num
        num = num - 1
    print("The factorial is", factorial)
