import sys

ranges = []
for line in sys.stdin:
    if line.strip() == '':
        break
    id_range = line.strip().split('-')
    start, end = int(id_range[0]), int(id_range[1])
    ranges.append([start, end])

total = 0
sorted_ranges = sorted(ranges, key=lambda r: r[0])
last_index = 0
for r in sorted_ranges:
    if r[1] <= last_index:
        continue

    start_index = max(last_index + 1, r[0])
    total += r[1] - start_index + 1
    # Update last_index
    last_index = r[1]

print(total)
