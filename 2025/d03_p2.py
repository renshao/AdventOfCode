import sys

def find_max(line: list, start_idx: int, end_idx: int):
    max_digit = 0
    max_index = start_idx
    # Find the largest digit and its index (including the last digit)
    for i in range(start_idx, end_idx + 1, 1):
        if line[i] > max_digit:
            max_digit = line[i]
            max_index = i
    return max_digit, max_index

total = 0
for line in sys.stdin:
    line_list = list(map(int, line.strip()))
    length = len(line_list)
    current_num = 0
    start_idx = 0
    for i in range(12, 0, -1):
        end_idx = length - i
        max_digit, pre_max_index = find_max(line_list, start_idx, end_idx)
        current_num = current_num * 10 + max_digit
        start_idx = pre_max_index + 1
    total += current_num

print(total)