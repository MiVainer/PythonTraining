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
print("Папа" in PhoneNumbers) #Проверка на вхождение '''

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
