import sys

lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

cols: list[int] = [1 for _ in lines[0]]

for y, line in enumerate([list(x.strip()) for x in lines][::-1]):
    for x, char in enumerate(line):
        if char == "^":
            cols[x] = cols[x-1] + cols[x+1]

        if char == "S":
            print(cols[x])
            sys.exit()
