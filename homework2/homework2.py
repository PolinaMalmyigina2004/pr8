while True:
  num1_str = input("Введите первое число: ")
  num2_str = input("Введите второе число: ")

  error_count = 0

  if num1_str[0] == "-" and num1_str[1:].isdigit():
    num1 = int(num1_str)
  elif num1_str.isdigit():
    num1 = int(num1_str)
  else:
    print("Ошибка: Введите первое число корректно.")
    error_count += 1

  if num2_str[0] == "-" and num2_str[1:].isdigit():
    num2 = int(num2_str)
  elif num2_str.isdigit():
    num2 = int(num2_str)
  else:
    print("Ошибка: Введите второе число корректно.")
    error_count += 1

  if error_count == 2:
    print("Ошибка: Введено два некорректных числа.")
    break # Завершаем цикл

  if error_count == 0:
    summa = num1 + num2
    print(f"Сумма чисел: {summa}")