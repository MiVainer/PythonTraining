'''# Работа со строками
chr(67) # Возвращает символ № 10 из таблицы Unicode

ord(c) # Возвращает номер символа c из таблицы Unicode.

a = 'This string is very big'
s = a[1:4] # У символов в строке есть свои индексы, символы начинаются с индекса 0
print('В указанном диапазоне находятся следующие символы: '+ s)

b = str(len(a))
print('В строке ' + b + ' символов')

c = input('Введи текст: ')
print(c)

# Форматирование строк
a = 'sobaka bivaet kusachei'
print(a.title())
print(a.upper())
print(a.lower())
print('--------------------------------------------------------------------------------------')

print("Это первая строка\nЭто вторая строка\nЭто третья строка")
print('--------------------------------------------------------------------------------------')

print("Messages:\n\tMessage1\n\tMessage2\n\tMessage3\nTHE END")
print('--------------------------------------------------------------------------------------')

b = "       , baba  Vera .             "
print(b)
b = b.strip() # Стирает пробелы справа и слева (rstrip - справа, lstrip - слева)
print(b)'''
'''b = b.strip(".") # Стираем точки
print(b)
b = b.strip(",") # Стираем запятые
print(b)
b = b.strip()
b = b.title()
print('Конечный результат форматирования: ' + b)
print('--------------------------------------------------------------------------------------')

print(f'Соединяем строки a и b: {a+b}') # Показан пример f-строки
print('--------------------------------------------------------------------------------------')

from string import Template # Пример строки пользовательского ввода с использование модуля string и класса Template
t = Template('Privet, $name')
print(t.substitute(name=input('Дружище! Как тебя зовут? ')))
print('--------------------------------------------------------------------------------------')

y = 'astralinux'
w = y[0:2]
e = y[-2:]
y = y.replace('as', '') # удалить или заменить значения строки (в данном случае заменяем символы пустым местом = удаляем)
y = y.replace('ux', '')
print(y)
print(w)
print(e)
print(f'{e}{y}{w}')
print('--------------------------------------------------------------------------------------')

g = 'astralinux'
e = g[::-1] #Переворачиваем строку в обратном порядке
print(g, e)

# Данная функция проверяет использовалась ли подстрока в строке
def search_subst(subst, st):
    if subst.lower() in st.lower():
        return 'Есть контакт!'
    else:
        return 'Мимо!'
print(search_subst('so', 'suroksoakasososika'))


# Функция по поиску индексов искомого элемента, входящего несколько раз в строку, вывод индексов списком.
def first_last(letter, st):
    b = []
    last_index = -1
    while True:
        try:
            last_index = st.index(letter, last_index+1)
        except ValueError:
            break
        else:
            b.append(last_index)
    return b

st = 'dsfjkhsldjfhjksdfbljsdfkbsfbsf'
letter = 's'
print(first_last(letter, st))

# Сформировать строку из элементов таблицы Unicod (Прописные и строчные буквы русского языка)
a = ""
for i in range(1040, 1103 + 1):
    a = a + chr(i)
    if chr(i) == 'Я':
        a = a + '\n'
print(*a, sep=', ')


def reverse_words(a):
    return " ".join(a.split()[::-1]) # Join объединяет любой итеррируемый объект в строку (в данном случае метод split переводит строку в список и меняет порядок слов.

a = "my name is Mihail"
print(reverse_words(a))'''

a = "my name is Mihail"
print(a.split()) # split преобразует в список
print("/".join(a.split()[::-1]))


