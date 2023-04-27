"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess, chardet
ping_resurs = [['ping', 'yandex.ru'],['ping', 'youtube.com']]
for ping_now in ping_resurs:
    print(f"пингуем {ping_now[1]}")
    ping_process = subprocess.Popen(ping_now, stdout=subprocess.PIPE)
    i = 0
    for line in ping_process.stdout:
        if i<3:
            code = chardet.detect(line)['encoding']
            print(f"кодировка ответа {code}")
            line = line.decode(code).encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            print(f"Прерываем чтобы не ждать")
            break