res = 0

while True:
    val = int(input('Enter a value: '))
    res += val
    if val == 0:
        break
print('Total: ', res)
