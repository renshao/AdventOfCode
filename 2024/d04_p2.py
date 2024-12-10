type Coord = tuple[int, int]

def check_window(matrix, top_left_coord: Coord) -> bool:
    x, y = top_left_coord
    return ((matrix[x + 1][y + 1] == 'A') and 


        ((matrix[x][y] == 'M' and matrix[x][y + 2] == 'M'
            and matrix[x + 2][y] == 'S' and matrix[x + 2][y + 2] == 'S')
            or

        (matrix[x][y] == 'S' and matrix[x][y + 2] == 'S'
            and matrix[x + 2][y] == 'M' and matrix[x + 2][y + 2] == 'M')
            or

        (matrix[x][y] == 'M' and matrix[x][y + 2] == 'S'
            and matrix[x + 2][y] == 'M' and matrix[x + 2][y + 2] == 'S')
            or

        (matrix[x][y] == 'S' and matrix[x][y + 2] == 'M'
            and matrix[x + 2][y] == 'S' and matrix[x + 2][y + 2] == 'M')))


matrix = []
with open('2024/d04_input.txt', 'r') as file:
    # Read each line in the file and conver to a list of ints
    for line in file:
        char_list = []
        for c in line.strip():
            char_list.append(c)
        matrix.append(char_list)

win_size = 3
matrix_size = len(matrix)

total = 0

# Sliding window
for i in range(matrix_size - win_size + 1):
    for j in range(matrix_size - win_size + 1):
        if check_window(matrix, (i, j)):
            total += 1

print(total)