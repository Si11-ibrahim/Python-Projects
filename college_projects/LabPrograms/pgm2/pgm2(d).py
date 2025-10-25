sentence = input('Enter a sentence with integers: ')

strings = []

integers = []

for i in sentence:
    if i.isdigit():
        integers.append(i)

    else:
        strings.append(i)

if len(strings) == 0:
    print('There is no strings in this sentence.')

else:
    print('Length of string value is ' + str(len(strings)))

if len(integers) == 0:
    print('There is no integers in this sentence.')

else:
    print('Length of string value is ' + str(len(integers)))
