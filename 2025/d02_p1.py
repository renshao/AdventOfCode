input_line = input()
prod_range_list = input_line.strip().split(',')
total = 0
for r in prod_range_list:
    if r == '':
        continue
    [start, end] = [int(token) for token in r.split('-')]
    for i in range(start, end + 1, 1):
        s = str(i)
        s_len = len(s)
        if s_len % 2 == 0:
            if s[0:(s_len // 2)] == s[(s_len // 2):]:
                total += i

print(total)
