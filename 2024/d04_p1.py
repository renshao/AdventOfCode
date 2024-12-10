type Coord = tuple[int, int]

# Given a list of coordinates, count how many XMAS in that list
def count_xmas_for_line(matrix, coords: list[Coord]):
    # If list size is less than 4, no need to check
    if len(coords) < 4:
        return 0
    
    total = 0
    # Use sliding window to find XMAS
    for i in range(len(coords) - 3):
        if ((matrix[coords[i][0]][coords[i][1]] == 'X'
            and matrix[coords[i + 1][0]][coords[i + 1][1]] == 'M'
            and matrix[coords[i + 2][0]][coords[i + 2][1]] == 'A'
            and matrix[coords[i + 3][0]][coords[i + 3][1]] == 'S')
            
            or
            
            (matrix[coords[i][0]][coords[i][1]] == 'S'
            and matrix[coords[i + 1][0]][coords[i + 1][1]] == 'A'
            and matrix[coords[i + 2][0]][coords[i + 2][1]] == 'M'
            and matrix[coords[i + 3][0]][coords[i + 3][1]] == 'X')):
            total += 1

    return total

def top_left_triangle(size) -> list[list[Coord]]:
    lines = []

    for i in range(size):
        coords = []
        for j in range(i + 1):
            coords.append((i - j, j))
        lines.append(coords)
    return lines

def bottom_right_triangle(size) -> list[list[Coord]]:
    lines = []

    for i in range(1, size, 1):
        coords = []
        for j in range(0, size - i):
            coords.append((size - 1 - j, i + j))
        lines.append(coords)
    return lines

def top_right_triangle(size) -> list[list[Coord]]:
    lines = []

    for i in range(size):
        coords = []
        for j in range(i + 1):
            coords.append((j, size - 1 - i + j))
        lines.append(coords)
    return lines

def bottom_left_triangle(size) -> list[list[Coord]]:
    lines = []

    for i in range(size - 1):
        coords = []
        for j in range(i + 1):
            coords.append((size - j - 1, i - j))
        lines.append(coords)
    return lines

matrix = []
with open('2024/d04_input.txt', 'r') as file:
    # Read each line in the file and conver to a list of ints
    for line in file:
        char_list = []
        for c in line.strip():
            char_list.append(c)
        matrix.append(char_list)

size = len(matrix)

total = 0

# First scan each horizontal line
for i in range(size):
    # Compute current line coords
    coords = []
    for j in range(size):
        coords.append((i, j))
    total += count_xmas_for_line(matrix, coords)

# Next scan each vertical line
for i in range(size):
    # Compute current line coords
    coords = []
    for j in range(size):
        coords.append((j, i))
    total += count_xmas_for_line(matrix, coords)

# Next scan diagnal /
for coords in top_left_triangle(size):
    total += count_xmas_for_line(matrix, coords)

for coords in bottom_right_triangle(size):
    total += count_xmas_for_line(matrix, coords)

for coords in top_right_triangle(size):
    total += count_xmas_for_line(matrix, coords)

for coords in bottom_left_triangle(size):
    total += count_xmas_for_line(matrix, coords)

print(total)