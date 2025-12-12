import sys

lines = []
for line in sys.stdin:
    tokens = line.strip().split()
    print(tokens)
    lines.append(tokens)

line_count = len(lines)
num_questions = len(lines[0])

total = 0
for i in range(num_questions):
    if lines[line_count - 1][i] == '*':
        answer = 1
        for j in range(0, line_count - 1):
            answer *= int(lines[j][i])
        total += answer

    elif lines[line_count - 1][i] == '+':
        answer = 0
        for j in range(0, line_count - 1):
            answer += int(lines[j][i])
        total += answer

print(total)