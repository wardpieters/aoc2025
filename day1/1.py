lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

dial = 50
count = 0

for line in lines:
    direction = line[0]
    clicks = int(line[1:].strip())

    if direction == 'L':
        dial = (dial - clicks) % 100
    elif direction == 'R':
        dial = (dial + clicks) % 100
    else:
        pass

    if dial == 0:
        count += 1

    # print(f"After {direction}{clicks}, dial is at {dial}")

print(count)