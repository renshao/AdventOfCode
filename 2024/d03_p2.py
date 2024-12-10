import re

with open('2024/d03_input.txt', 'r') as file:
    memory_content = file.read().replace('\n', '')

total = 0
enabled = True
for matched_str in re.finditer(r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)', memory_content):
    s = matched_str.group() 
    if s == 'do()':
        enabled = True
    elif s == "don't()":
        enabled = False
    else:
        if enabled:
            total += int(matched_str.group(1)) * int(matched_str.group(2))

print(total)