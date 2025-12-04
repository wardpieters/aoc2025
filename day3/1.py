banks = []
with open('input.txt', 'r') as f:
    banks = f.readlines()

total = 0

for x in banks:
    bank = [int(val) for val in x.strip()]
    largest = 0
    largest_index = -1

    current_index = 0
    for val in bank[:-1]:
        if val > largest:
            largest = val
            largest_index = current_index
        
        current_index += 1

    rest_bank = bank[largest_index+1:]
    first = largest

    current_index = 0
    largest = 0
    for val in rest_bank:
        if val > largest:
            largest = val
        
        current_index += 1

    bank_val = int(f"{first}{largest}")

    total += int(bank_val)
    print()

print(total)