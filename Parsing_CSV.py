# -------------------------#
# ---Program by MiVainer---#
import csv
import re

with open("/home/mihail/parsing/SharkTest.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",") # Создаем объект reader, указываем символ-разделитель ","
    count = 0 # Счётчик для прохождения по строкам
    for row in file_reader:
        if count == 0: # Для самой ерхней строки выводим названия столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            if row[4] == "TCP":
                print(f'Адрес источника - {row[2]}\nАдрес назначения - {row[3]}\n') # Берём второй и третий столбец из файла

        count += 1 # Переходим к следующей строке

    print(f'Всего в файле {count} строк.')


