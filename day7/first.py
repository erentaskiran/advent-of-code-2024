def isEqual(target, values, nowValue, i):
    if (i >= len(values)):
        return target == nowValue
    return isEqual(target, values, nowValue*values[i], i+1) or isEqual(target, values, nowValue+values[i], i+1)


with open("input1.txt", "r") as file:
    content = [line.strip().split(": ") for line in file.readlines()]
ans = 0
for line in content:
    target = int(line[0])
    values = [int(m) for m in line[1].split(" ")]
    if isEqual(target, values, 0, 0):
        ans += target


print(ans)
