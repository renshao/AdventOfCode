list1 = []
list2 = []
with open('2024/d01_input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        numbers = list(map(int, line.strip().split()))
        list1.append(numbers[0])
        list2.append(numbers[1])

list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print(total)