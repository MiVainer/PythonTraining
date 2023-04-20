import re

inputfile = f"/var/log/{input('Введи имя файла для парсинга в папке /var/log- ')}"
myfile = open(inputfile, mode='r', encoding='ascii')
text = myfile.read() # Прочитаем файл полностью
search_text = r"SerialNumber:+ +\w+" #Сгенерировал на сайте regex101.com
results = re.findall(search_text, text)

print('Вот тебе все подключения usb устройств')
for num, i in enumerate(results):
    print(num, i)


