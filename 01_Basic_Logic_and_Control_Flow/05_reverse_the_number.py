number = int(input("Enter a number: "))
if number == 0:
    print("The reverse of the number is: 0")
    exit()
elif number > 0:
    sign = +1
else:
    sign = -1
number = abs(number)
reverse = 0
while number > 0:
    reverse = (reverse * 10) + (number % 10)
    number = number // 10
print("The reverse of the number is:", sign * reverse)
