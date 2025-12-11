file_path = "d01_input.txt"

dial = 50
count = 0

with open(file_path, 'r') as file:
    for line in file:
        direction = line[0]
        num = int(line[1:].strip())

        if direction == 'L':
            dial -= num
        elif direction == 'R':
            dial += num

        dial = dial % 100
        if dial == 0:
            count += 1


print(count)