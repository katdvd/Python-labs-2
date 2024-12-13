from task_1 import (Book, Car, UserProfile)

if __name__ == "__main__":
    # Создание объектов для всех классов
    try:
        book = Book("1984", "George Orwell", 328)
        car = Car("Tesla", "model y", 50.0)
        profile = UserProfile("john_doe", 150, 45)


    except ValueError as e:
        print('Ошибка: неправильные данные')

    # Проверка методов с некорректными аргументами

    try:
        # Попытка создания книги с отрицательным количеством страниц
        invalid_book = Book("1984", "George Orwell", -328)  # Некорректный аргумент
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        # Попытка создания машины с пустым названием
        invalid_car = Car("Tesla", "model y", -50.0)  # Некорректный аргумент
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        # Попытка создания профиля с некорректными данными
        invalid_profile = UserProfile("john_doe", -150, 45)  # Некорректный аргумент
    except ValueError as e:
        print('Ошибка: неправильные данные')