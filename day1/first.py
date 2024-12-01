with open("input1.txt", "r") as file:
    lines = file.readlines()


list1, list2 = [], []

for e in lines:
    inputs = e.split("  ")
    list1.append(int(inputs[0]))
    list2.append(int(inputs[1]))

list1.sort()
list2.sort()

ans = 0
for i in range(len(list2)):
    ans += abs(list1[i]-list2[i])
print(ans)
