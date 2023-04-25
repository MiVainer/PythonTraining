#!/bin/bash
# -------------------------#
# ---Program by MiVainer---#

import shutil
import os
import sys


# script1.py mylog.txt 10 5

if (len(sys.argv) < 4):
    print('Введены не все аргументы')
    exit(1)

file_name = sys.argv[1]
limitsize = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if (os.path.isfile(file_name) == True):
    logfile_size = os.stat(file_name).st_size # размер файла в байтах
    logfile_size = logfile_size / 1024 # Переводим в килобайты

    if (logfile_size >= limitsize):
        if (logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):
                src = file_name + '_' + str(currentFileNum - 1)
                dst = file_name + '_' + str(currentFileNum)
                if (os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
            shutil.copyfile(file_name, file_name + '_1')
            print("Copied: ", file_name, " to ",file_name + "_1")
        myfile = open(file_name, 'w')
        myfile.close()

