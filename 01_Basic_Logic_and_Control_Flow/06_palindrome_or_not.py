number = int(input("Enter a number: "))

if number < 0:
    print("The number is not a palindrome.")
elif number == 0:
    print("The number is a palindrome.")
else:
    temp = number
    reverse = 0
    while temp > 0:
        reverse = (reverse*10) + (temp % 10)
        temp = temp//10
    if number == reverse:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
