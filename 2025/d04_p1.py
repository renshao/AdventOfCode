import sys

def is_location_valid(row, col, row_count, col_count):
    return 0 <= row < row_count and 0 <= col < col_count

def count_rolls(grids, row, col, row_count, col_count):
    count = 0
    # up left
    if is_location_valid(row - 1, col - 1, row_count, col_count):
        if grids[row - 1][col - 1] == '@':
            count += 1

    # up
    if is_location_valid(row - 1, col, row_count, col_count):
        if grids[row - 1][col] == '@':
            count += 1

    # up right
    if is_location_valid(row - 1, col + 1, row_count, col_count):
        if grids[row - 1][col + 1] == '@':
            count += 1

    # left
    if is_location_valid(row, col - 1, row_count, col_count):
        if grids[row][col - 1] == '@':
            count += 1

    # right
    if is_location_valid(row, col + 1, row_count, col_count):
        if grids[row][col + 1] == '@':
            count += 1

    # down left
    if is_location_valid(row + 1, col - 1, row_count, col_count):
        if grids[row + 1][col - 1] == '@':
            count += 1

    # down
    if is_location_valid(row + 1, col, row_count, col_count):
        if grids[row + 1][col] == '@':
            count += 1

    # down right
    if is_location_valid(row + 1, col + 1, row_count, col_count):
        if grids[row + 1][col + 1] == '@':
            count += 1

    return count

grids = []
for line in sys.stdin:
    grids.append(line.strip())

row_count = len(grids)
col_count = len(grids[0])

total = 0
for i in range(row_count):
    for j in range(col_count):
        if grids[i][j] == '@':
            count = count_rolls(grids, i, j, row_count, col_count)
            if count < 4:
                total += 1

print(total)
