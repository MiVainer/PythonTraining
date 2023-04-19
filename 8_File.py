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

inputfile = f"/var/log/{input('Введи имя файла для парсинга в папке /var/log- ')}"
outputfile = f"/home/mihail/parsing/{input('Введи имя файла для сохранения результата в каталоге /home/mihail/parsing- ')}"

search_str = "SerialNumber: "
myfile = open(inputfile, mode='r', encoding='ascii')
myfile1 = open(outputfile, mode='w', encoding='ascii')
for line in myfile:
    if search_str in line:
        myfile1.write(line + '\n')

myfile.close()
myfile1.close()