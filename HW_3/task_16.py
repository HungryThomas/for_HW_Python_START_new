n = int(input('Введите количество элементов в массиве: '))
array = []
for i in range(n):
    array.append(i)
print(array)
x = int(input('Введите число, о котором Вы хотите узнать, сколько раз оно повторяется в массиве: '))
count = 0
for i in range(n):
    if array[i] == x:
        count += 1
if count == 0:
    print('Такого числа нет в массиве')
else:
    print('Число посторяется столько раз в массиве: ')
    print(count)
