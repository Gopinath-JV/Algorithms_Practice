num = int(input("Enter the number upto which we need to print fibonacci series: "))
if num < 0:
    print("Cannot print fibbonacci series as the value is less than 0")
else:
    first = 0
    second = 1
    limit = num
    while first <= limit:
        print(first)
        next_num = first + second
        first = second
        second = next_num
