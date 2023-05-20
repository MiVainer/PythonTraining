# -------------------------#
# ---Program by MiVainer---#


# Сортировка

list = [1, 8, -2, 4, 0, 15, 11, 12, 9, 64]
for i in range(0, len(list)-1):
    for k in range(0, len(list)-1):
        if list[k] > list[k+1]:
            list[k], list[k+1] = list[k+1], list[k]
print(list)
