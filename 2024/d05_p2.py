class Rule:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    
    def check(self, a: int, b: int):
        if a == self.a and b == self.b:
            return True
        elif b == self.a and a == self.b:
            return False
        else:
            return True

def is_seq_valid(a: int, b: int, rules: list[Rule]):
    for rule in rules:
        if not rule.check(a, b):
            return False
    return True

rules = []
updates = []
with open('2024/d05_input.txt', 'r') as file:
    is_rule = True
    # Read each line in the file
    for line in file:
        line_cleaned = line.strip()
        if line_cleaned == '':
            is_rule = False
            continue

        if is_rule:
            numbers = list(map(int, line_cleaned.split('|')))
            rules.append(Rule(numbers[0], numbers[1]))
        else:
            numbers = list(map(int, line_cleaned.split(',')))
            updates.append(numbers)

total = 0
# Evaluate each update
for update in updates:
    is_valid = True
    for i in range(len(update) - 1):
        if not is_seq_valid(update[i], update[i + 1], rules):
            is_valid = False
            break
    if is_valid:
        total += update[len(update) // 2]
        
print(total)
