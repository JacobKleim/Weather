import requests


city_names = ['Санкт-Петербург', 'svo', 'Череповец']
params = {'T': '', 'n': '', 'M': '', '2': '', 'lang': 'ru'}


def get_weather(city):
    url_template = ('https://wttr.in/{}')
    url = url_template.format(city)
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def print_weather_in_cities(cities):
    for city in cities:
        print(get_weather(city))


if __name__ == '__main__':
    print_weather_in_cities(city_names)
