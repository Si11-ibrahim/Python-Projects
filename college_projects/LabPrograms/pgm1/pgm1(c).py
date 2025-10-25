sen = input('Enter a Sentence: ')

vow = ['a', 'e', 'i', 'o', 'u']
print('Vowels removed: ', end='')
for i in sen:
    if i in vow:
        continue
    else:
        print(i, end='')
