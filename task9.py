num = int(input('Введите ваше число: '))
result = 0


while num != 0:
    next_num = int(input('Введите ваше число: '))
    if next_num != 0 and num < next_num:
        result += 1
    num = next_num
print(result)