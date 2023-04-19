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

def search_subst(subst, st):
    if subst.lower() in st.lower():
        return 'Есть контакт!'
    else:
        return 'Мимо!'


def unique_list(numbers):
    new_numbers = []
    sort_numbers = sorted(numbers)
    print(f'Вот сортированный по возрастанию искомый список - {sort_numbers}')
    for i in range(1, len(sort_numbers)-1):
        if sort_numbers[i] != sort_numbers[i-1]:
            new_numbers.append(sort_numbers[i])
    return new_numbers