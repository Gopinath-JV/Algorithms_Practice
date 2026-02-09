# first i need to enter a string value

# then i calculate its length

# now i need to start saving the string characterstics in reverse order


word = input("Enter any string: ")
reverse = ''
word_index = len(word) - 1
while word_index >= 0:
    reverse = reverse + word[word_index]
    word_index = word_index - 1
print("reverse of the string is: ", reverse)
