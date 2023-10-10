n = int(input('Введите число N: '))
action = 0

for i in range(1, n + 1):
    barrier = n
    if i**i < n:
        print(i**i)
