# Problem 02:Check whether a number is even or odd

# Input
a = int(input("Enter a number: "))

# Logic
if a % 2 == 0:
    result = 'even'
else:
    result = 'odd'

# Output
print("The number", a, "is:", result)
