n = int(input('Введите количество элементов в массиве: '))
array = []
for i in range(n):
    array.append(i)
print(array)
x = float(input('Введите число, о котором Вы хотите узнать, к какому числу в массиве оно находится ближе всего по своему значению: '))
minimum = abs(x-array[0])
for i in range(n):
    if (abs(x-array[i])) < minimum:
        minimum = abs(x-array[i])
for i in range(n):
    if minimum == abs(x-array[i]):
        print('ближайший по величине элемент в массиве: ')
        print(array[i])
