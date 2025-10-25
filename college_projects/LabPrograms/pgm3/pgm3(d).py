var = input("Enter a string: ")

words = []
word = ''
for i in var:
    word += i
    if i == ' ':
        words.append(word.strip())
        word = ''
if not words:
    words.append(word)

print(words)