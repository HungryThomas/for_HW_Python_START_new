n = int(input('Введите случайное положительное целое шестизначное число: '))
lastthree = 0
while n>=1000:
    digit = n%10
    lastthree+=digit
    n//=10
firstthree = 0
while n>0:
    digit = n%10
    firstthree+=digit
    n//=10
if lastthree == firstthree:
    print('Yes, lucky!')
else:
    print('No, unlucky!')