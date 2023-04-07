# Различные задачи по работе с циклами

# Поиск суммы чисел в заданном диапазоне
'''sum = 0
for i in range(int(input('Введи начальное число диапазона - ')), int(input('Введи последнее число диапазона - '))):
    sum = sum + i
print(f'Сумма чисел = {sum}')

# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список, в котором содержатся только те числа, которые больше 5 по модулю.

def more_then_five(lst):
    new_lst = []
    for i in lst:
        if i > 5 or i < -5:
            new_lst.append(i)
    return new_lst

lst = [1, 5, 6, 10, -3, -9, -7, -1, 12, 22]
print(f'Вот новый список - {more_then_five(lst)}')

#Напишите программу на Python, чтобы найти те числа, которые делятся на 7 и кратны 5, между 1500 и 2700 (оба включены).

lst = []
for i in range(1500, 2700+1):
    if (i % 7 == 0) and (i % 5 == 0):
        lst.append(i)
print(lst)

# Написать программу для построения шаблона из звездочек в виде квадрата
k = int(input('Введи размер стороны квадрата - '))
for i in range(1, k+1):
    print('\t')
    for j in range(1, k+1):
        print('*', end="")

# Напишите программу на Python для печати букв алфавита 'Z'
result = ""
for row in range(0, 7):
    for column in range(0, 7):
        if ((row == 0 or row == 6) and column <= 6 and column >= 0) or row+column == 6:
            result = result + "*"
        else:
            result = result + " "
    result = result + "\n"

print(result)

# Напишите программу на Python для печати букв алфавита 'T'
result = ""
for row in range(0, 6):
    for column in range(0, 7):
        if (row == 0 and column <= 6 and column >= 0) or row > 0 and column == 3:
            result = result + "*"
        else:
            result = result + " "
    result = result + "\n"

print(result)'''






