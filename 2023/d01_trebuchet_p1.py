# Compute the int value of the given char.
# If c is not a digit, returns 0, else return the digit's int value.
# E.g. for 'a' it returns 0, for '2' it returns 2
def compute_char_value(c: str) -> int:
    ascii_value = ord(c)
    # 48 is the ASCII value of '0', 57 is the ASCII value of '9'
    if ascii_value > 48 and ascii_value <= 57:
        return ascii_value - 48
    else:
        return 0

def compute_line_score(line: str):
    left_digit = 0
    right_digit = 0
    # First scan from left to right, find first non-zero char
    for c in line:
        digit_value = compute_char_value(c)
        if digit_value > 0:
            left_digit = digit_value
            break

    # Then scan from right to left, find first non-zero char
    for c in reversed(line):
        digit_value = compute_char_value(c)
        if digit_value > 0:
            right_digit = digit_value
            break
    
    return left_digit * 10 + right_digit

total = 0
with open('2023/d01_input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Call strip() to remove the trailing newline character
        total += compute_line_score(line.strip())

print(total)
