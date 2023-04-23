import psycopg2

outputfile = f"/home/mihail/parsing/{input('Введи имя файла для сохранения результата в каталоге /home/mihail/parsing- ')}"
myfile = open(outputfile, mode='w', encoding='utf8')

connection = psycopg2.connect(database="demo",
                                user="mivainer",
                                password="sms2851140",
                                host="172.17.0.2",
                                port="5432")


cursor = connection.cursor()


mySQLQuery = ("""
                SELECT airport_name, city, timezone
                FROM airports_data
                """)
# Получение данных по указанному запросу
try:
    cursor.execute(mySQLQuery)
except Exception as err:
    print('Ошибка при выполнении запроса к БД PostgreSQL:', err)


results = cursor.fetchall() # только для чтения данных

for num, row in enumerate(results):
    airport_name = row[0]['ru']
    city = row[1]['ru']
    timezone = row[2]
    myfile.write(f'Запись №{num}\nАэропорт - {airport_name}\nГород - {city}\nВременная зона - {timezone}\n\n')
    print(f'Запись №{num}\nАэропорт - {airport_name}\nГород - {city}\nВременная зона - {timezone}\n\n')

connection.close()
myfile.close()