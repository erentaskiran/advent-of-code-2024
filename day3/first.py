import re

with open("input1.txt", "r") as file:
    content = file.read()

regex = r"mul\(\d+,\d+\)"

matches = re.findall(regex, content)

product = 0
for match in matches:
    numbers = match.split(",")
    num1, num2 = int(numbers[0][4:]), int(numbers[1][:-1])
    product += num1 * num2

print(product)
