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
        for sec_len in range(s_len // 2, 0, -1):
            if s_len % sec_len == 0:
                all_sec_same = True
                first_sec = s[0:sec_len]
                for j in range(sec_len, s_len, sec_len):
                    if s[j:(j + sec_len)] != first_sec:
                        all_sec_same = False
                        break
                if all_sec_same:
                    total += i
                    break

print(total)