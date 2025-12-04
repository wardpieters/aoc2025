input = ""
with open('input.txt', 'r') as f:
    input = f.read()

count = 0

for line in input.split(","):
    [begin, end] = line.split("-", 2)
    first = int(begin)
    last = int(end)

    i = first

    while i <= last:
        if len(str(i)) % 2 == 1:
            i+=1
            continue

        chars = list(str(i))
        chars_length = len(chars)

        valid = True

        for x in range(0, int(chars_length / 2)):
            char_a = chars[x]
            char_b = chars[int(chars_length / 2) + x]
            
            if char_a != char_b:
                valid = False
                break

            x += 1
        
        if valid:
            count += i if valid else 0
        
        i+=1

print()
print(count)