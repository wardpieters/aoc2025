lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

count = 0

start = 0
ranges: list[list[int]] = []
for i, line in enumerate(lines):
    if line == "\n":
        start = i + 1
        break

    ranges.append(list(map(int, line.strip().split("-", 2))))

for id in [int(line.strip()) for line in lines[start:]]:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            count += 1
            break

print(count)
