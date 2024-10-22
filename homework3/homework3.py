def draw_square(symbol):
    for i in range(10):
        print(symbol*10)
            
while True:
    user_input = input("Введите символ для рисования квадрата:")
    if user_input == '*':
        draw_square(user_input)
        break
    else:
        print("Ошибка! Пожалуйста, введите только символ '*'.")