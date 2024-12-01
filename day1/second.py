with open("input2.txt", "r") as file:
    lines = file.readlines()


list1, list2 = [], []

for e in lines:
    inputs = e.split("  ")
    list1.append(int(inputs[0]))
    list2.append(int(inputs[1]))

dic = {}

for i in range(len(list2)):
    dic[list2[i]] = dic.get(list2[i], 0) + 1

ans = 0
for i in list1:
    ans += i * dic.get(i, 0)
print(ans)
