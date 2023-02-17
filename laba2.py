import requests
city = "Moscow, RU"
appid = "a811c25ed0f4441944cbfb18756a5c38"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на день:")
print('Скорость ветра', data['wind']['speed'])
print('Видимость', data['visibility'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
for i in data['list']:
    print('Прогноз на неделю')
    print('Дата', i['dt_txt'])
    print('Скорость ветра', i['wind']['speed'])
    print('Видимость', i['visibility'])
    print('_________________________')

