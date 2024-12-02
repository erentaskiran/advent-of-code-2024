def is_sorted(numbers):
    isDecreasing = True
    isAscending = True

    for i in range(1, len(numbers)):
        diff = abs(numbers[i] - numbers[i - 1])
        if diff < 1 or diff > 3:
            isDecreasing = False
            isAscending = False
            break
        if numbers[i] >= numbers[i - 1]:
            isDecreasing = False
        if numbers[i] <= numbers[i - 1]:
            isAscending = False

    if isDecreasing or isAscending:
        return True
    return False


with open("input2.txt", "r") as file:
    lines = file.readlines()

liste = [list(map(int, line.split())) for line in lines]
ans = 0

for numbers in liste:
    if is_sorted(numbers):
        ans += 1
        continue

    for j in range(len(numbers)):
        temp = numbers[:j] + numbers[j + 1:]
        if is_sorted(temp):
            ans += 1
            break

print(ans)
