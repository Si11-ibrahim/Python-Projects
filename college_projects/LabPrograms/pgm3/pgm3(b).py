lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
subList = []
start = int(input("Enter the starting index: "))
end = int(input("Enter the ending index: "))

for i in range(start, end + 1):
    subList.append(lst[i])

print(subList)