# Работа со словарями
# Ключи - неизменный тип данных (числа, строка, кортеж) , значения - изменяемые типы данных
'''PhoneNumbers = {}
PhoneNumbers["Михаил"] = "8-923-733-32-87" # В данном случае ключ и значение являются строками, но они могут быть другими типами данных
PhoneNumbers["Мама"] = "8-912-111-23-33"
PhoneNumbers["Папа"] = "8-991-222-42-44"
PhoneNumbers["Надя"] = "8-923-734-32-87"
PhoneNumbers["Андрей"] = "8-916-635-23-44"
print(PhoneNumbers) # Вывод всего словаря (ключ-значение)
#print("Номер абонента - "+ PhoneNumbers[input("Введи название аобнента - ")])
print(PhoneNumbers.keys()) # Вывод ключей словаря
print(PhoneNumbers.values()) # Вывод значений словаря
print(PhoneNumbers.__len__()) # Вывод размера словаря
print(*sorted(PhoneNumbers), sep = ', ')
del(PhoneNumbers["Михаил"]) # Удаляем элемент словаря
print(PhoneNumbers)
#PhoneNumbers.clear() # Удаляем все элементы словаря
#print(PhoneNumbers)
print("Папа" in PhoneNumbers) #Проверка на вхождение

enemy = {
            'loc_x': 70,
            'loc_y': 50,
            'color': 'red',
            'health': 100,
            'name': 'Ivan'
}

enemy['rank'] = 'capitan' # Добавляем элемент в словарь
enemy['awards'] = ['Suvorova', 'Zhukova'] # Добавляем элемент в словарь
print('Первый враг', enemy)

enemy['loc_x'] = enemy['loc_x'] + 20 # Изменяем величины словаря
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'

print('Враг изменён', enemy)

all_enemies = []
for i in range(0, 10):
    all_enemies.append(enemy.copy()) # Добавляем словари в список

for k in all_enemies:
    print('Много врагов', k) # выводим словари

all_enemies[3]['health'] = 10 # Вносим изменения в 3 элемент списка
all_enemies[5]['name'] = 'Aleksandr'# Вносим изменения в 5 элемент списка
all_enemies[8]['rank'] = 'leitenant' # Вносим изменения в 8 элемент списка

print('-----------------------------------------------------------------')

for k in all_enemies:
    print('Враги изменены', k)

# Задачи
# Объединить словари в один
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic4 = dict(list(dic1.items())+list(dic2.items())+list(dic3.items()))
print(dic4)

# Проверить есть ли ключ в словаре
enemy = {
            'loc_x': 70,
            'loc_y': 50,
            'color': 'red',
            'health': 100,
            'name': 'Ivan',
            'weight': 70,
            'might': 'low'
}
def key_in_dict(x):
     if x in enemy:
         print('This key is exist')
     else:
         print('Key is not exist')
     return

key_in_dict('nam')

# Написать программу для перебора словаря

enemy = {
            'loc_x': 70,
            'loc_y': 50,
            'color': 'red',
            'health': 100,
            'name': 'Ivan',
            'weight': 70,
            'might': 'low'
}
for dict_key, dict_volue in enemy.items():
    print(dict_key,'->', dict_volue)

# Напишите скрипт Python для генерации и печати словаря, который содержит число (от 1 до n) в форме (x, x * x).

dict = {a: a*a for a in range(5)}
print(f'Вот такой словарь у тебя получился {dict}')

# Напишите скрипт Python для печати словаря, в котором ключи - это числа от 1 до 15 (оба включены), а значения - квадрат ключей.

dict = {a: a*a for a in range(1, 16)}
print(f'Вот такой словарь у тебя получился {dict}')

# Напишите скрипт Python для объединения двух словарей Python.
a = {'a': 10, 'b': 20}
b = {'c': 30}
a.update(b)
print(a)

# Напишите программу на Python для суммирования всех элементов в словаре.
# 1 метод
a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
sum = 0
for i in a.values():
    sum = sum+i
print('1 метод - ', sum)
# 2 метод
a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
print('Второй метод - ', sum(a.values()))

# Напишите программу на Python для отображения двух списков в словарь.
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

# Напишите программу на Python для сортировки словаря по ключу.
a = {'n': 50, 'a': 10, 'b': 20, 'k': 100}
sorted_tuple = sorted(a.items(), key=lambda x: x[0])
print(dict(sorted_tuple))

#Напишите программу на Python, чтобы получить максимальное и минимальное значение в словаре.
a = {'n': 50, 'a': 10, 'b': 20, 'k': 100}
ma = max(a.values())
mi = min(a.values())
print(f'Максимальное значение - {ma}\nМинимальное значение - {mi}')'''



