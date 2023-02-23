s = int(input('Введите первую подсказку (сумму чисел): '))
p = int(input('Введите вторую подсказку (произведение чисел): '))
for i in range(s):
    for j in range(p):
        if s == i + j and p == i * j:
            print(i,j)