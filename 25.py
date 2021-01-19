max_cur_del = 0
max2 = 0
max = 0
max_del = []
max2_del = []
count_del = 0

for num in range(394480, 394540 + 1):
    cur_del = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cur_del += 1
            max2 = max
            max = i
    if cur_del > max_cur_del:
        count_del = 1
        max_cur_del = cur_del
        max_del.clear()
        max2_del.clear()
        max_del.append(num)
        max2_del.append(max2)
    elif cur_del == max_cur_del:
        count_del += 1
        max_del.append(num)
        max2_del.append(max2)

for i in range(1, count_del + 1):
    print(str(i) + ' ' + str(max_cur_del) + ' ' + str(max_del[i - 1]) + ' ' + str(max2_del[i - 1]))
