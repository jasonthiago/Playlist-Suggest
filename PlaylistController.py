import configparser
import requests
import sys


def get_playlist(location):
    temperature = get_local_temperature(location)
    print(temperature)

    if temperature >= 25.0:
        playlist_id = get_playlist_id('pop')
    elif temperature >= 10.0:
        playlist_id = get_playlist_id('rock')
    else:
        playlist_id = get_playlist_id('classic')

    url = "https://api.deezer.com/playlist/{}/tracks".format(playlist_id)
    r = requests.get(url)
    return r.json()


def get_local_temperature(location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, get_api_key())
    r = requests.get(url)
    return r.json()['main']['temp']


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweather']['key']


def get_playlist_id(music_style):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['playlist'][music_style]