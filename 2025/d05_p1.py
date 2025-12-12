import sys

range_completed = False
ranges = []
ids = []

for line in sys.stdin:
    if line.strip() == '':
        range_completed = True
        continue

    if not range_completed:
        id_range = line.strip().split('-')
        start, end = int(id_range[0]), int(id_range[1])
        ranges.append([start, end])

    else:
        ids.append(int(line.strip()))


total = 0
# Check each ingredient ID
for ing_id in ids:
    in_range = False
    for r in ranges:
        if r[0] <= ing_id <= r[1]:
            in_range = True
            break
    if in_range:
        total += 1

print(total)
