
import re

with open("input2.txt", "r") as file:
    content = file.read()

regex = r"don't\(\)|do\(\)|mul\(\d+,\d+\)"

matches = re.findall(regex, content)

isDo = True

product = 0
for match in matches:
    if (match == "don't()"):
        isDo = False
    elif (match == "do()"):
        isDo = True
    elif (isDo):
        numbers = match.split(",")
        num1, num2 = int(numbers[0][4:]), int(numbers[1][:-1])
        product += num1 * num2


print(product)
