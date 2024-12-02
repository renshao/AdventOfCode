def is_report_safe(numbers: list) -> bool:
    # First compute delta between first two numbers
    first_delta = numbers[0] - numbers[1]
    if first_delta == 0:
        return False
    
    # Find out all deltas
    for i in range(1, len(numbers), 1):
        delta = numbers[i - 1] - numbers[i]
        
        # If delta and first_delta have different sign, is unsafe
        if (first_delta ^ delta) < 0:
            return False
        
        delta_abs = abs(delta)
        if delta_abs == 0 or delta_abs > 3:
            return False
    return True

safe_report_count = 0
with open('2024/d02_input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        numbers = list(map(int, line.strip().split()))
        if is_report_safe(numbers):
            safe_report_count += 1
        else:
            for i in range(len(numbers)):
                current = numbers.copy()
                current.pop(i)
                if is_report_safe(current):
                    safe_report_count += 1
                    break

print(safe_report_count)
