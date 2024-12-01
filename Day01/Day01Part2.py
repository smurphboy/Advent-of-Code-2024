left = []
right = []
with open('Day01/input.txt') as file:
    for line in file:
        left_nb, right_nb = line.strip().split()
        right.append(int(right_nb))
        left.append(int(left_nb))

    similarity_score = 0
    for nb in left:
        similarity_score += nb * right.count(nb)

    print (similarity_score)
