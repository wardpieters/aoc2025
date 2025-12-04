input = ""
with open('input.txt', 'r') as f:
    input = f.read()

invalid_numbers: set[int] = set()

for line in input.split(","):
    [begin, end] = line.split("-", 2)
    first = int(begin)
    last = int(end)

    i = first

    while i <= last:
        if len(str(i)) == 1:
            i+=1
            continue

        # If all digits are the same, add to count.
        if len(set(str(i))) == 1:
            invalid_numbers.add(i)
            i+=1

            continue

        chars = list(str(i))
        chars_length = len(chars)

        valid = False

        longest_substr = ''
        x_range = int(chars_length / 2) + 1
        for x in range(0, x_range):
            char = chars[x]
            # Initialize
            if not longest_substr:
                longest_substr = char
                continue
        
            longest_substr += char
            
            # If sequence has endend, validate if this is repeating
            substring_count = str(i).count(longest_substr)
            if len(longest_substr) != len(str(i)) and substring_count * len(longest_substr) == len(str(i)):
                valid = True
                break

        if valid:
            invalid_numbers.add(i)

        i+=1

print()
print(sum(invalid_numbers))
