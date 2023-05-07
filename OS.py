# -------------------------#
# ---Program by MiVainer---#
import os

print(os.name) # название настоящей ОС
print(os.getlogin()) # Имя пользователя, вошедшего в систему
print(os.getpid())
print(os.uname()) # Информация об ОС
print(os.getcwd()) # Текущая рабочая дирректория
print(*os.listdir(path="."), sep='\n') # Список файлов в искомом каталоге