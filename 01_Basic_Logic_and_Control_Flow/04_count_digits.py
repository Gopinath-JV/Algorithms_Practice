a = int(input("Enter a number: "))
if a == 0:
    print("The number has 1 digit.")
else:
    a = abs(a)
    count = 0
    while a > 0:
        a = a//10
        count = count + 1
    print("The number has", count, "digits.")
