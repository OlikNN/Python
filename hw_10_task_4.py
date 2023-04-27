"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
print()
words = ['разработка', 'администрирование', 'protocol', 'standard']
for word in words:
    enc = word.encode('utf-8')
    print(f"'{word}' из строки в байты '{enc}'", type(enc))
    dec = bytes.decode(enc, 'utf-8')
    print(f"'{word}' из байтов в строку '{dec}'", type(dec))
    print()
