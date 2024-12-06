import sys
sys.setrecursionlimit(10000)
ans = 0


def helper(content, i, j, sum, directioni, directionj):
    global ans
    if (i >= len(content) or i < 0 or j < 0 or j >= len(content[0])):
        ans = max(ans, sum)
        return
    if (i+directioni >= len(content) or i+directioni < 0 or j + directionj < 0 or j + directionj >= len(content[0])):
        ans = max(ans, sum+1)
        return
    if (content[i+directioni][j + directionj]) == "#":
        if (directioni == 0 and directionj == 1):
            directionj = 0
            directioni = 1
        elif (directioni == 0 and directionj == -1):
            directionj = 0
            directioni = -1
        elif (directioni == 1 and directionj == 0):
            directionj = -1
            directioni = 0
        elif (directioni == -1 and directionj == 0):
            directionj = 1
            directioni = 0
    if (not content[i][j] == "X"):
        sum += 1
        content[i] = content[i][:j] + "X" + content[i][j+1:]
    helper(content, i+directioni, j+directionj, sum, directioni, directionj)


with open("input1.txt", "r") as file:
    content = [line.strip() for line in file.readlines()]

k, n = 0, 0
for i in range(len(content)):
    for j in range(len(content[0])):
        if (content[i][j] == "^"):
            k, n = i, j


helper(content, k, n, 0, -1, 0)

print(ans)
