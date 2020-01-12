import os
import re
import json
import urllib.request


def create_note(path, t, c):
    os.chdir(path)
    add_note(t, c)

def read_notes(path):
    os.chdir(path)
    with open('notes.json', 'r') as f:
        notes = json.load(f)
        for i in notes:
            print(notes[i])

def add_note(t, c):
    try:
        with open('notes.json', 'r+') as data_file:
            notes = json.load(data_file)
            count = len(notes['notes'])
            notes['notes'].update({count+1:{t:c}})
        with open('notes.json', 'w') as data_file:
            json.dump(notes, data_file)
    except:
        with open('notes.json', 'r+') as f:
            json.dump({'notes':{1:{t:c}}}, f)


def get_city_info():
    url = 'http://ipinfo.io/json'
    response = urllib.request.urlopen(url)
    data = json.load(response)
    city = data['city']
    return city

def weather_api(key):
    city_name = get_city_info()
    response = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+key)
    data = json.load(response)
    return data


def news_api(kw, key):
    response = urllib.request.urlopen("https://newsapi.org/v2/top-headlines?q="+kw+"&apiKey="+key)
    data = json.load(response)
    return data