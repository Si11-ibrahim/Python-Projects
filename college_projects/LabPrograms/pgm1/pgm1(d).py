i = 0

val = int(input("Enter the length: "))

while i <= val:
    if i % 2 == 0:
        print(i, 'is an Even value.\n')

    else:
        print(i, 'is an odd value.\n')

    i += 1

print('\n---- End of loop -----')
