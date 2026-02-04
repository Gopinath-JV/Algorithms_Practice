a = int(input("enter the number:"))
if a < 2:
    print("it is not a prime number")
else:
    for n in range(2, int(a**0.5)+1):
        if a % n == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")
