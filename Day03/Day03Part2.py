import re

with open('Day03/input.txt') as file:
    groups = re.findall(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", file.read())
    mults = [x for row in groups for x in row if x != ""]
    sum = 0
    enabled = True
    for mult in mults:
        if(mult == "do()"):
            enabled = True
            continue
        if(mult == "don't()"):
            enabled = False
            continue
        if(not enabled):
            continue
        a,b = str(mult).replace("mul(", "").replace(")", "").split(",")
        sum += int(a)*int(b)
    print(sum)

