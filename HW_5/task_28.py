a = int(input('Введите первое целое неотрицательное число для сложения: '))
b = int(input('Введите второе целое неотрицательное число для сложения: '))
def summa(a,b):
    if a == 0:
        return b
    return summa(a - 1, b + 1)
print(summa(a,b))