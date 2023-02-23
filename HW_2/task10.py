n = int(input('Введите количество монеток: '))
count_head = 0
count_tail = 0
for i in range(n):
    x = int(input('Введите статус лежащей монетки (0 - орел, 1 - решка): '))
    if x == 0:
        count_head += 1
    else:
        count_tail += 1
if count_head > count_tail:
    print('Минимальное количество монеток, которое надо перевернуть: ')
    print(count_tail)
if count_tail > count_head:
    print('Минимальное количество монеток, которое надо перевернуть: ')
    print(count_head)