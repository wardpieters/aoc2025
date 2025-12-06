lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

count = 0
data = [list(line.strip("\n")) for line in lines]

operator = ""
col_result = 0
for i in range(0, len(max(data, key=len))):
    col = [x[i] for x in data]
    col_val = "".join(col).replace(" ", "")
    
    if col[-1] == "*":
        operator = "*"
    if col[-1] == "+":
        operator = "+"

    if col_val == "":
        count += col_result
        operator = ""
        col_result = 0
        continue

    if not col_result:
        col_result = int(col_val.replace("*", "").replace("+", ""))
    elif operator == "+":
        col_result += int(col_val)
    elif operator == "*":
        col_result *= int(col_val) 
    
count += col_result
print(count)