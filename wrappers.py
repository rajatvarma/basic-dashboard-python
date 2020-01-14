import os
import re
import json
import urllib.request


def create_note(path, t, c):
    os.chdir(path)
    add_note(t, c)

def create_task(path, t, c):
    os.chdir(path)
    add_task(t, c)




def read_notes(path, isNotes, isTasks):
    os.chdir(path)
    if isNotes:
        fileName = 'notes.json'
    if isTasks:
        fileName = 'tasks.json'    
    with open(fileName, 'r') as f:
        output = json.load(f)
    return output


def add_task(t, c):
    try:
        with open('tasks.json', 'r+') as data_file:
            tasks = json.load(data_file)
            count = len(tasks['tasks'])
            tasks['tasks'].update({count+1:{t:c}})
        with open('tasks.json', 'w') as data_file:
            json.dump(tasks, data_file)
    except:
        with open('tasks.json', 'r+') as f:
            json.dump({'tasks':{1:{t:c}}}, f)



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
