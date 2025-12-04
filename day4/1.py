import sys
import numpy

lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0
rows = [list(line.strip()) for line in lines]
matrix = numpy.matrix(rows)

def get_adjecent_values(x, y):
    adjecent = []

    # above
    if x > 0:
        adjecent.append(matrix[x-1, y])
    # below
    if x < matrix.shape[0] - 1:
        adjecent.append(matrix[x+1, y])
    # left
    if y > 0:
        adjecent.append(matrix[x, y-1])
    # right
    if y < matrix.shape[1] - 1:
        adjecent.append(matrix[x, y+1])

    # diagonal top-left
    if x > 0 and y > 0:
        adjecent.append(matrix[x-1, y-1])
    # diagonal top-right
    if x > 0 and y < matrix.shape[1] - 1:
        adjecent.append(matrix[x-1, y+1])
    # diagonal bottom-left
    if x < matrix.shape[0] - 1 and y > 0:
        adjecent.append(matrix[x+1, y-1])
    # diagonal bottom-right
    if x < matrix.shape[0] - 1 and y < matrix.shape[1] - 1:
        adjecent.append(matrix[x+1, y+1])

    return adjecent

for x, line in enumerate(rows):
    for y, roll in enumerate(line):
        if roll == ".":
            continue

        adjecent = get_adjecent_values(x, y)
        rolls_count = sum(1 for r in adjecent if r == "@")
        
        if rolls_count < 4:
            total += 1

print(total)
