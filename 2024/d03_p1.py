import re

def compute_line_score(line):
    line_total = 0
    for matched_str in re.finditer(r'mul\((\d+),(\d+)\)', line):
        line_total += int(matched_str.group(1)) * int(matched_str.group(2))
    return line_total

total = 0
with open('2024/d03_input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        total += compute_line_score(line.strip())

print(total)
