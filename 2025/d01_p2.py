file_path = "test.txt"

dial = 50
count = 0

with open(file_path, 'r') as file:
    for line in file:
        direction = line[0]
        num = int(line[1:].strip())

        if direction == 'L':
            if num >= dial:
                count += (num - dial) // 100
                if dial != 0:
                    count += 1
                dial = (dial - num) % 100
            else:
                dial -= num
        elif direction == 'R':
            dial += num
            if dial >= 100:
                count += dial // 100
                dial = dial % 100
        print(dial, count)


