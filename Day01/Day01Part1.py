left = []
right = []
zipped = []
with open('Day01/input.txt') as file:
    for line in file:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    zipped = (zip(sorted(left), sorted(right)))
    summed = 0
    for pair in zipped:
        summed = summed + abs(pair[0] - pair[1])
    print (summed)