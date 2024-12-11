def count_digits(n: int) -> int:
    n = n // 10
    count = 1
    while n != 0:
        n = n // 10
        count += 1
    return count

def blink(input: list[int]) -> list[int]:
    output = []
    # Rule 1
    for n in input:
        if n == 0:
            output.append(1)
        else:
            digits = count_digits(n)
            if digits % 2 == 0:
                half_digits = digits // 2
                power = pow(10, half_digits)
                output.append(n // power)
                output.append(n % power)
            else:
                output.append(n * 2024)
    return output


with open('2024/d11_input.txt', 'r') as file:
    numbers = list(map(int, file.read().rstrip().split()))

for i in range(5):
    print(i)
    numbers = blink(numbers)

print(len(numbers))
