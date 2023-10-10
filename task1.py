string = ["X", "Y", "O"] # Создание массива
def counter(): # Создание функции для вычисления кратчайшего пути
    x_index = None # Создание переменной
    y_index = None # Создание переменной
    for index, value in enumerate(string): # Добавление 2-ух переменных для индекса, и значения индекса(в данном случае буквы) и последующий их перебор через функция enumerate
        if value == "X": # Условие для проверки
            x_index = index # Присвоение переменной текущий индекс буквы "X"
        elif value == "Y":
            y_index = index # Присвоение переменной текущий индекс буквы "Y"
    if x_index is not None and y_index is not None: # Условие для проверки
            result = abs(y_index - x_index - 1) # Вычисление кратчайшего пути между "X" и "Y"
            print(result) # Вывод результата на экран
    else:
        x_index is None or y_index is None # Условние для проверки в случае несоблюдения первого условия
        print(123)


counter() # Вызов функции 