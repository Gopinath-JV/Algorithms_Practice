import array as arr

numbers = arr.array(
    'i', map(int, input("Enter marks (e.g. 80,90): ").split(",")))

length = len(numbers)
if len(numbers) == 0:
    print("Array is empty")
else:
    index = 1
    small = numbers[0]
    while (index < length):
        if numbers[index] < small:
            small = numbers[index]
        index += 1
    print("the smallest element in an array is:", small)
