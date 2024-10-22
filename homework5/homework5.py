def is_number(s):
    """Проверяет, является ли строка числом (включая отрицательные и десятичные числа)."""
    if s.count('.') > 1:  # Проверка на больше одной десятичной точки
        return False
    if s.replace('.', '', 1).replace('-', '', 1).isdigit():  # Убираем одну точку и минус, проверяем цифры
        return True
    return False

total_sum = 0.0  # Переменная для хранения суммы

while True:
    user_input = input("Введите число (или 'stop'/'end' для завершения): ")

    if user_input.lower() in ['stop', 'end']:  # Проверка на команды завершения
        break

    if is_number(user_input):  # Проверка на корректность ввода числа
        total_sum += float(user_input)  # Преобразуем строку в число и добавляем к сумме
    else:
        print("Ошибка: Введите корректное число.")

print(f"Сумма введенных чисел: {total_sum}")