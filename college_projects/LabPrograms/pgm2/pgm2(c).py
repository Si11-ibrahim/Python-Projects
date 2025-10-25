till = int(input("What is the length of fibonacci? ")) + 1


v1 = 0
v2 = 1
print(v1)
for i in range(2, till):
    v3 = v1 + v2
    v1 = v2
    v2 = v3
    print(v3)
