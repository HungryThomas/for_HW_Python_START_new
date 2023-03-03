n = int(input('Введите число кустов: '))
array = list()
for i in range(n):
    x = int(input('Введите объем урожая: '))
    array.append(x)
array_count = list()
for i in range(len(array) - 1):
    array_count.append(array[i - 1] + array[i] + array[i + 1])
array_count.append(array[-2] + array[-1] + array[0])
print(max(array_count))