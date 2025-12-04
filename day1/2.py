lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

dial = 50
crossings = 0

for line in lines:
    direction = line[0]
    clicks = int(line[1:].strip())
    
    for _ in range(abs(clicks)):
        if direction == 'R':
            dial = (dial + 1) % 100
        else:
            dial = (dial - 1) % 100

        if dial == 0:
            crossings += 1

print("part 2:", crossings)
