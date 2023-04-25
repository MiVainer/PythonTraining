#!/bin/bash
# -------------------------#
# ---Program by MiVainer---#

# Скрипт для очистки старых файлов

import os
import time

DAYS = 5 # Максимальное количество дней хранения файлов
FOLDERS = [
            "/home/mihail/Archive/Folder1",
            "/home/mihail/Archive/Folder2",
            "/home/mihail/Archive/Folder3",
            "/home/mihail/Archive/Folder4"
]

TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILE = 0
TOTAL_DELETED_DIRS = 0

nowtime = time.time() # Время в секундах в настоящий момент
agetime = nowtime - 60*60*24*DAYS # Вычитаем время хранения в секундах

def delete_old_files(folder):
    #Удалить файлы старше заданного количества дней
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            filename = os.path.join(path, file)
            filetime = os.path.getmtime(filename)
            if filetime < agetime:
                sizefile = os.path.getsize(filename)
                TOTAL_DELETED_SIZE += sizefile # Считаем сумму удаляемых файлов
                TOTAL_DELETED_FILE += 1 # Считаем количество удаляемых файлов
                print("Удалены файлы: ", str(filename))
                os.remove(filename) #Удаление файла

def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            print("Удаляем пустую дирректорию: ", str(path))
            os.rmdir(path)

#============================MAIN====================================#
starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder) #Удаление старых файлов
    delete_empty_dir(folder) # Удаление пустых директорий

finishtime = time.asctime()

print("-----------------------------------------------------------------")
print("START TIME: ", str(starttime))
print("Total Deleted size: ", str(TOTAL_DELETED_SIZE), " b")
print("Total Deleted files: ", str(TOTAL_DELETED_FILE), " b")
print("Total Deleted empty folders: ", str(TOTAL_DELETED_DIRS), " b")
print("FINISH TIME: ", str(finishtime))
print("-----------------------------------------------------------------")


