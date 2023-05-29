import requests
import csv
import json


URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    btc = {'name': data['chartName'],
           'update_time': data['time']['updated'],
           'disclaimer': data['disclaimer'],
           'usd_rate': data['bpi']['USD']['rate'],
           'gbp_rate': data['bpi']['GBP']['rate'],
           'eur_rate': data['bpi']['EUR']['rate']}

    with open(r'C:\Users\vorot\Desktop\Костя\Питон\Пет проекты\Проект 1\btc_data.csv', 'a') as csvfile:

        # Создание объекта для записи данных в файл CSV в формате словаря
        writer = csv.DictWriter(csvfile, fieldnames=btc.keys())

        # Проверка, нужно ли записать заголовки
        if csvfile.tell() == 0:
            writer.writeheader()

        # Запись данных в файл CSV
        writer.writerow(btc)




