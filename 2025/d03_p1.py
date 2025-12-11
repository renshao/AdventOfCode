import sys

def find_max(line: list):
    max = 0
    max_index = 0
    # Find largest digit and its index (exclude the last digit)
    for index, n in enumerate(line[:-1]):
        if n > max:
            max = n
            max_index = index
    # Next find the largest digit between max_index and the end of the line
    max2 = 0
    for n in line[max_index + 1:]:
        if n > max2:
            max2 = n
    return max * 10 + max2

total = 0
for line in sys.stdin:
    total += find_max(list(map(int, line.strip())))

print(total)