
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



list4 = [1, 2, 3, 4, 5, 6]

list4.reverse()
print(list4)


list1.insert(4, 0)
list1.insert(10, 0)
print(list1)


my_list = [1, 2, 3, 4, 5, 6]
del my_list[-1]
del my_list[2]
my_list.clear()
print(my_list)

# arrange in ascending and descending
list5 = [6, 5, 4, 9, 11]
print("original list: ", list5)
list5.sort()
print("Ascending order: ", list5)
my_list.sort(reverse=True)
print("Descending order: ", list5)
