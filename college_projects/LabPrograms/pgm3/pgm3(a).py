# Middle value from list


lstSize = int(input('Enter the size of the list: '))
lst = []
for i in range(lstSize):
    lst.append(input('Enter an input: '))

midIndex = len(lst) / 2 - 1

if len(lst) % 2 == 0:
    print('Middle elements are ', lst[int(midIndex)], ', ', lst[int(midIndex + 1)])

else:
    print('Middle element is ', lst[int(midIndex.__abs__() + 1)])
