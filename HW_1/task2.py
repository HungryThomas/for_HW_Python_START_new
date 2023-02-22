n = int(input('Введите трехзначное целое положительное число: '))
summ = 0
while n>0:
    digit = n%10
    summ += digit
    n//=10
print(summ)