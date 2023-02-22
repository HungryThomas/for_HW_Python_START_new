n = input('Введите случайное положительное шестизначное число: ')
summOfFirstThree = int(n[0]) + int(n[1]) + int(n[2])
summOfLastThree = int(n[3]) + int(n[4]) + int(n[5])
if summOfFirstThree == summOfLastThree:
    print('Yes')
else:
    print('No')