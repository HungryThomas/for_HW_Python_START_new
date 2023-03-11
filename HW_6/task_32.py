list = [-5, 18, 6, 0, -10, 4, -1, -8, 12, 15, 7]
min_number = int(input('Введите минимальное значение: '))
max_number = int(input('Введите максимальное значение: '))
for i in range(len(list)):
    if min_number <= list[i] and list[i] <= max_number:
        print(i)