'''inputfile = "./venv/names"

outputfile = "./venv/out_names"
myfile = open(inputfile, mode='r', encoding='ascii')
myfile1 = open(outputfile, mode='a', encoding='ascii') # mode = w при закрытии файла и последующем открытии записывает файл по новому, не добавляет, mode = a всегда добавляет

search_char = input()

for line in myfile:
    if search_char in line:
        myfile1.write("Searching string - " + (line.strip()).title() + '\n')

myfile.close()
myfile1.close()'''

# Пишем скрипт для выборки из логов подключенных флэш-накопителей к ПЭВМ с датой, временем, серийником

