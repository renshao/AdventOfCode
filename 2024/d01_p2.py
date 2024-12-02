list1 = []
list2 = []
with open('2024/d01_input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        numbers = list(map(int, line.strip().split()))
        list1.append(numbers[0])
        list2.append(numbers[1])

list2_map = {}
for n in list2:
    count = list2_map.setdefault(n, 0)
    list2_map[n] = count + 1

total = 0
for n in list1:
    total += n * list2_map.get(n, 0)

print(total)
