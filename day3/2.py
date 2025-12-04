banks = []
with open('input.txt', 'r') as f:
    banks = f.readlines()

total = 0

for x in banks:
    bank = [int(val) for val in x.strip()]
    power: list[int] = []
    
    for current_index, val in enumerate(bank):
        rest_length = len(bank) - current_index

        if len(power) == 0:
            power.append(val)
            continue
        
        new_val = False
        for i, power_val in enumerate(power):
            if val > power_val and rest_length >= 12 - i:
                power[i] = val
                power = power[0:i+1]
                new_val = True
                break

        if new_val:
            continue

        if len(power) < 12:
            power.append(val)
            continue

    power_str = ''.join([str(x) for x in power])
    power_int = int(power_str)

    total += int(power_int)

print()
print(total)