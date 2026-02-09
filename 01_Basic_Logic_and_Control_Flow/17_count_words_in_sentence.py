sentence = input("Enter the sentence: ")
index = 0
count = 0

while index < len(sentence):
    if sentence[index] != ' ' and (index == 0 or sentence[index - 1] == ' '):
        count = count + 1
    index = index + 1

print("the total number of words in the sentence is:", count)
