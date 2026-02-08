word = input(
    "Enter a word of your choice to calculate the total number of vowels in it: ")
index = 0
count = 0
while index < len(word):
    if (word[index].lower() in 'aeiou'):
        count = count + 1
    index = index + 1
print("Total number of vowels in the given word is: ", count)
