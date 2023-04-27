"""
Задание 6.

Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимо
"""

import locale

text = ['сетевое программирование', 'сокет', 'декоратор']

def_coding = locale.getpreferredencoding()

print(f'Кодировка по умолчанию {def_coding}')

with open('test_file.txt', 'w+', encoding='utf-8') as f_n:
    for i in text:
        f_n.write(i + '\n')
    f_n.seek(0)

print(f_n)




with open('test_file.txt', 'r', encoding='utf-8') as f_n:
    for i in f_n:
        print(i)

    f_n.seek(0)