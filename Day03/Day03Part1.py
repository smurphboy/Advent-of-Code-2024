import re

with open('Day03/input.txt') as file:
    mults = re.findall(r"mul\(\d{1,3},\d{1,3}\)", file.read())
    sum = 0
    for mult in mults:
        a,b = str(mult).replace("mul(", "").replace(")", "").split(",")
        sum += int(a)*int(b)
    print(sum)