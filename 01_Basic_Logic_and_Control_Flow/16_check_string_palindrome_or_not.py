word = input("Enter any string: ")
reverse = ''
word = word.lower()
word_index = len(word) - 1
while word_index >= 0:
    reverse = reverse + word[word_index]
    word_index = word_index - 1
if word == reverse:
    print("given string is a palindrome")
else:
    print("given string is not a palindrome")
