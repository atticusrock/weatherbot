import requests

def temp(city):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid=ace288eb77dee4fbd15df6ea4c6d7e65'.format(city))
    d = response.json()
    if 'main' in d:
        return int(d['main']['temp']) - 273
    else:
        return None
#
# while True:
#     town = input()
#     t = temp(town)
#     print('В городе {} температура {}'.format(town, t))