# Данные о диске и книге
# disk_capacity_mb = 1.44  # Объем дискеты в мегабайтах
# pages_per_book = 100      # Количество страниц в книге
# lines_per_page = 50       # Количество строк на странице
# chars_per_line = 25       # Количество символов в строке
# bytes_per_char = 4        # Количество байт для хранения одного символа
#
# # Конвертация объема дискеты в байты
# disk_capacity_bytes = disk_capacity_mb * 1024 * 1024  # 1 Мб = 1024 Кб = 1024 * 1024 байт
#
# # Расчет объема одной книги в байтах
# volume_per_book_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char
#
# # Расчет количества книг, которые можно поместить на дискету
# number_of_books = disk_capacity_bytes // volume_per_book_bytes
#
# # Вывод результата
# print(f"Количество одинаковых книг, которые можно поместить на дискету: {number_of_books}")

# Задача 2
# Радиус круга и сторону квадрата
# radius = 5
# side = 5
#
# # Расчет площади круга и длины окружности
# circle_area = 3.14 * (radius ** 2)
# circumference = 2 * 3.14 * radius
#
# # Округление значений до 2 знаков после запятой
# circle_area_rounded = round(circle_area, 2)
# circumference_rounded = round(circumference, 2)
#
# # Расчет периметра квадрата и площади квадрата
# square_perimeter = 4 * side
# square_area = side ** 2
#
# # Округление значений до 2 знаков после запятой (для квадратов это не обязательно, но для единообразия)
# square_perimeter_rounded = round(square_perimeter, 2)
# square_area_rounded = round(square_area, 2)
#
# # Печать результатов
# print(f"Площадь круга: {circle_area_rounded}")
# print(f"Длина окружности: {circumference_rounded}")
# print(f"Периметр квадрата: {square_perimeter_rounded}")
# print(f"Площадь квадрата: {square_area_rounded}")

# Задача 3
# # Формирование строки из повторяющихся чисел
# str_numbers = '0' * 20 + '1' * 50 + '2' * 30
#
# # Вывод значения переменной str_numbers
# print(str_numbers)
