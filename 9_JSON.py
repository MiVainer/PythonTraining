import json
filename = 'user_settings.txt'
myfile1 = open(filename, mode='w', encoding='ascii')
human1 = {
    'HumanName': 'Vladimir Putin',
    'Health': 100,
    'Titul': ["Korol", "Som", "Lom"]
}

human2 = {
    'HumanName': 'Vladimir Zelensky',
    'Health': 5,
    'Titul': ["Akter", "Kloun"]
}

humans = []
humans.append(human1)
humans.append(human2)

# Сохраняем в JSON

json.dump(humans, myfile1)
myfile1.close()

# Загружаем из JSON

myfile1 = open(filename, mode='r', encoding='ascii')
json_data = json.load(myfile1)

for human in json_data:
    print('Human name is ', str(human['HumanName']))
    print('Health is ', str(human['Health']))
    print('His titul is ', str(human['Titul'][0]))
    print('His titul is ', str(human['Titul'][1]))
    print('-------------------------------------')