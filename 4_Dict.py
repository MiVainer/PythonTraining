# Работа со словарями
# Ключи - неизменный тип данных (числа, строка, кортеж) , значения - изменяемые типы данных
PhoneNumbers = {}
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