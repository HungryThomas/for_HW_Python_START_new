n = int(input('Введите случайное положительное целое шестизначное число: '))
LastThree = 0
while n>=1000:
    digit = n%10
    LastThree+=digit
    n//=10
FirstThree = 0
while n>0:
    digit = n%10
    FirstThree+=digit
    n//=10
if LastThree == FirstThree:
    print('Yes, lucky!')
else:
    print('No, unlucky!')