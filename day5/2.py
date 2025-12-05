lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

count = 0
ranges: list[list[int]] = []

for i, line in enumerate(lines):
    if line == "\n":
        break

    ranges.append(list(map(int, line.strip().split("-", 2))))

ranges.sort(key=lambda interval: interval[0])
merged_ranges = [ranges[0]]
for current in ranges:
    previous = merged_ranges[-1]
    if current[0] <= previous[1]:
        previous[1] = max(previous[1], current[1])
    else:
        merged_ranges.append(current)

for range in merged_ranges:
    count += range[1] - range[0] + 1

print(count)
