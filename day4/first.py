def check_word(content, i, j, dx, dy, target):
    word = ""
    for k in range(len(target)):
        x, y = i + k * dx, j + k * dy
        if 0 <= x < len(content[0]) and 0 <= y < len(content):
            word += content[y][x]
        else:
            return False
    return word == target


with open("input1.txt", "r") as file:
    content = [line.strip() for line in file.readlines()]

ans = 0
target_words = ["XMAS", "SAMX"]

directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

for j in range(len(content)):
    for i in range(len(content[0])):
        for dx, dy in directions:
            for target in target_words:
                if check_word(content, i, j, dx, dy, target):
                    ans += 1

print(ans)
