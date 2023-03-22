# Реализовать структуру «Рейтинг», представляющую собой не
# возрастающий набор натуральных чисел
# (каждый элемент ряда меньше или равен предыдущему).
#
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].


value = int(input("Ведите новый элемент рейтинга: "))
my_list = [7, 5, 3, 3, 2]

if value <= 0:
    print('Введите натуральное число')
else:
    max_value = max(my_list)
    if value > max_value:
        my_list.insert(0, value)
    elif value in my_list:
        my_list.insert(my_list.index(value), value)
    else:
        my_list.append(value)
    print(my_list)
