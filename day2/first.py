with open("input1.txt", "r") as file:
    lines = file.readlines()

liste = []

for line in lines:
    numbers = list(map(int, line.split()))
    liste.append(numbers)

ans = 0

for numbers in liste:
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
        ans += 1

print(ans)
