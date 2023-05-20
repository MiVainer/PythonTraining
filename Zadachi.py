# -------------------------#
# ---Program by MiVainer---#
'''
#1
a = ['papa', 1, 'Sabl9a', 'rOBOt', 'KroT', 9, 'SoFt']

a = a[::-1]
print(a)'''

'''# 2

def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
lst = ['papa', 1, 'Sabl9a', 'rOBOt', 'KroT', 9, 'SoFt']
print(change(lst))'''

'''#3
def to_lists(*args):
    return list(args)

print(to_lists(1, 'sok', 'stroKa', 4))'''

'''#4

a = [1, -1, 0, 5, 99, 6, 323, 7, -122, 8, 42, 999, 64, 37, 59, 4, 6]
print(f'выводим максимальное значение с помощью функции max - {max(a)}')
a = sorted(a)
print(f'Вот максимальное значение от сортированного списка - {a[-1]}')
print(f'Искомое значение - {a[-1]//len(a)}')'''

# 5
'''

def all_eq(lst):
    max_item = max(lst, key=lambda x: len(x)) # Выводит элемент списка с максимальной длиной
    max_len = len(max_item)
    return [item.ljust(max_len, '_') for item in lst]

print(all_eq(['ambassador', 'sort', 'file', 'som', 'sobaken', 'morj', 'korobka', 'host']))'''
'''
a = 'adjahj fak  lafjlkajf  alkfja akf'
print(*a.split(), sep=", ")'''

# Словари
'''
list = ['abra', 'kadabra', 'sobaka', 'kusaka', 'kot', 'fedor']
dict = dict(zip(list, list))
print(dict)
'''

'''
dict = {'first_one': 'we can do it'}
def biggest_dict(**kwargs):
    dict.update(**kwargs)

biggest_dict(name = 'Sam', k = 10, b = 20, c = 40, color = 'red', rod = 'susu')
print(dict)
'''

'''
def count_it(sequence):
    num = list(map(int, sequence.split()))
    slovar = dict(zip(num, str(len(num))))
    return slovar

sequence = '1 2 3 7 8 0 1 2 7 4 4 6 2 3 7 4 8'
print(count_it(sequence))
'''

# В этой задаче вы должны, учитывая строку, заменить каждую букву её позицией в алфавите.
# Если что-то в тексте не является буквой, игнорируйте это и не возвращайте.
# «a» = 1, «b» = 2 и т.д.

'''alpha="The sunset sets at twelve o' clock."
a = []
for i in alpha.lower():
    if i.isalpha() == True:
        a.append(str(ord(i)-96))

print(alpha)
print(", ".join(a))'''

# функция, которая путём перестановки цифр возвращает наибольшее число

def BiggerNum(num):
    a = "".join(sorted(list(str(num)))[::-1])
    return a

num = 123777
print(BiggerNum(num))








