#Методы работы со списками
''''# Находим длину списка (количество элементов)
a = ['dsg', 'sgdjsk', 'qwqe', 'oot', 'tyre', 'qwe', '5', '3', '9', '0', '123', '4', '6']
print(len(a))

# Удаляем элемент из списка
del a[-1] # удалили последний элемент
print(a)

# Удаляем элемент по его имени
a.remove('oot')
print(a)

# append - добавляет элемент в конце списка
a = ['one', 'alo']
a.append('stttt')
print(a)

# insert - добавляет элемент в указанную позицию
a = ['one', 'alo']
a.insert(1, 'srt')
print(a)

# extend - добавляем больше одного элемента в список
a = ['one', 'alo']
b = ['usr', 'lib', 'sin']
a.extend(b)
print(a)

# index - возвращаем индекс элемента
a = ['dsg', 'sgdjsk', 'qwqe', 'oot', 'tyre', 'qwe', '5', '3', '9', '0', '123', '4', '6']
print(a.index('qwe'))

# pop - удаляем элемент, можно также использовать remove, del.
a = ['dsg', 'sgdjsk', 'qwqe', 'oot', 'tyre', 'qwe', '5', '3', '9', '0', '123', '4', '6']
rm = a.pop(9)
print(a)
print(rm)



# sort - сортирует список в возрастающем порядке
a = ['dsg', 'sgdjsk', 'qwqe', 'oot', 'tyre', 'qwe', '5', '3', '9', '0', '123', '4', '6']
a.sort()
print(a)

# reverse - переворачивает список
a = ['dsg', 'sgdjsk', 'qwqe', 'oot', 'tyre', 'qwe', '5', '3', '9', '0', '123', '4', '6']
a.reverse()
print(a)'''



#Практика!!!
# Задача № 1. Вывести все элементы меньше 5.
'''SP = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = []
for i in SP:
    if i < 5:
        a.append(i)
print(a)'''

# Задача № 2. Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for k in b:
        if i == k:
            c.append(i)
print(c)'''

'''# Задача № 3. Написать функцию, которая принимает список элементов и возвращает только целые числа.

def return_only_integer(lst):
    integers = []
    for i in lst:
        if type(i) is int:
            integers.append(i)
    return integers

lst = [1, 5, 7, 'a', 'ww', '22']
print(return_only_integer(lst))'''

# Перечисляем элементы списка в нормальном виде
'''a = ['dsg', 'sgdjsk', 'qwqe', 'oot', 'tyre', 'qwe', '5', '3', '9', '0', '123', '4', '6']
print(*a, sep = ", ") # Знак * используется для разделения элементов списка выбранным символом

for i in a:
    print(i.title())

# Создаём список
new_list = list(range(1, 10))
print(*new_list, sep=", ")

print(*new_list[::-1]) #Переворачиваем список

print(max(new_list)) # Максимальное значение в списке
print(sum(new_list)) # Суммирует элементы списка 


def unique_list(numbers):
    new_numbers = []
    sort_numbers = sorted(numbers)
    print(f'Вот сортированный по возрастанию искомый список - {sort_numbers}')
    for i in range(1, len(sort_numbers)-1):
        if sort_numbers[i] != sort_numbers[i-1]:
            new_numbers.append(sort_numbers[i])
    return new_numbers 

numbers = [1, 2, 3, 3, 5, 7, 0, 2, 4, 5, 9, 7, 8]
print(unique_list(numbers)) 


# Задача. На входе список с повторящюимися числами, вывести отсортированный список с уникальными числами

new_numbers = []
sort_numbers = sorted(numbers)
print(f'Вот сортированный по возрастанию искомый список - {sort_numbers}')
for i in range(0, len(sort_numbers)-1):
    if (sort_numbers[i] != sort_numbers[i - 1]) and (sort_numbers[i] != sort_numbers[i+1]):
        new_numbers.append(sort_numbers[i])
print(new_numbers) 

numbers = [1, 2, 3, 3, 5, 7, 0, 2, 4, 5, 9, 7, 8]
numbers = set(numbers)
numbers = list(numbers)
numbers = sorted(numbers)
print(numbers)'''

