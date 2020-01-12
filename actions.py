import urllib.request
import wrappers
import json
import random

wapikey = "6283614a6e2dacc9cda470ae9de25568"
napikey = "4918c606562845aa8feb315affce0afb"


def weather():
    data = wrappers.weather_api(wapikey)
    current_temperature = round(float(data["main"]["temp"])-273.15, 2)
    maximum_temperature = round(float(data["main"]["temp_max"])-273.15, 2)
    minimum_temperature = round(float(data["main"]["temp_min"])-273.15, 2)
    humidity = data["main"]["humidity"]
    output = {"Current Temperature": current_temperature, "Minimum Temperature": minimum_temperature, "Maximum Temperature":maximum_temperature, "Humidity":humidity}
    return output

def news(query):
    data = wrappers.news_api(query, napikey)
    if data['totalResults'] == 0:
        output = "No results found for " + query
    else:
        output = []
        for i in range(10):
            source = data["articles"][i]["source"]["name"]
            title = data["articles"][i]["title"]
            output.append([source, title])
    return output


def notes(path, c):
    if c == True:
        title = input("Enter a title: ")
        content = input("Write your notes. (DO NOT USE ENTER KEY UNTIL YOU HAVE FINISHED WRITING THE NOTE)")
        wrappers.create_note(path, title, content)
    elif c == False:
        wrappers.read_notes(path)


def hangman():
    word_list = ['book', 'trophy', 'science', 'programming','python', 'mathematics', 'google', 'condition','power', 'water', 'studio', 'deploy']
    current_word = random.choice(word_list)
    print("Enter a letter")
    guesses = ""
    turns = 7
    while turns > 0:
        failed=0
        for char in current_word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed+=1
        print()
        if failed==0:
            print("You Win!")
            print("The word is: ", current_word)
            break
        guess=input("Guess a character: ")
        guesses+=guess
        if guess not in current_word:
            turns-=1
            print("Wrong")
            print("You have ",turns," more guesses")
            if turns==0:
                break
