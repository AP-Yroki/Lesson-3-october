n = int(input('Введите натуральное число для ступенек: '))
letter = 0

if n > 0:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='', sep='')