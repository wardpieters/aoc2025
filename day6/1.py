import numpy


lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

count = 0

data = [[x for x in line.strip().split(" ") if x] for line in lines]
matrix = numpy.rot90(data, 3).tolist()

for row in matrix:
    row_result = 0
    operator = row[0]

    for value in row[1:]:
        if row_result == 0:
            row_result = int(value)
            continue

        if operator == "+":
            row_result += int(value)
        else:
            row_result *= int(value)

    count += row_result

print(count)