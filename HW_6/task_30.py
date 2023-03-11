a = int(input('Введите первый элемент регрессии: '))
d = int(input('Введите шаг/разность: '))
n = int(input('Введите количество элементов: '))
def progress(a,d,n):
    if n > 0:
        print(a, end = ' ')
        progress(a + d, d, n - 1)

progress(a,d,n)