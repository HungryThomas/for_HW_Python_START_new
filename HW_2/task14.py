n = int(input('Введите положительное целое число: '))
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1