def is_number(s):
    if s.count('.') > 1:  # Проверка на больше одной десятичной точки
        return False
    if s.replace('.', '', 1).replace('-', '', 1).isdigit():  # Убираем одну точку и минус, проверяем цифры
        return True
    return False

while True:
    a_str = input("Введите первое число (a): ")
    b_str = input("Введите второе число (b): ")

    if not is_number(a_str) and not is_number(b_str):
        print("Ошибка: Введено два некорректных числа.")
        break  # Завершаем цикл

    if not is_number(a_str):
        print("Ошибка: Введите первое число корректно.")
        continue

    if not is_number(b_str):
        print("Ошибка: Введите второе число корректно.")
        continue

    a = float(a_str)
    b = float(b_str)

    # Находим целые числа между a и b
    start = int(min(a, b)) + 1
    end = int(max(a, b))

    if start < end:
        print("Целые числа между a и b:")
        for i in range(start, end):
            print(i, end=" ")
    else:
        print("Нет целых чисел между a и b.")

    print()  # Добавляем пустую строку после вывода чисел

