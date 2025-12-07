lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

count: int = 0
beams: set[int] = set()

for y, line in enumerate([list(x.strip()) for x in lines]):
    for x, char in enumerate(line):
        if char == "S":
            beams.add(x)
            continue

        if char == "^" and x in beams:
            count+=1
            beams.remove(x)
            beams.add(x-1)
            beams.add(x+1)

print(count)