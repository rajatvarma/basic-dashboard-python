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
    elif data['totalResults'] > 10:
        output = []
        for i in range(10):
            source = data["articles"][i]["source"]["name"]
            title = data["articles"][i]["title"]
            output.append([source, title])
    else:
        output = []
        for i in range(data['totalResults']):
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
        notes = wrappers.read_notes(path, True, False)
        for i in notes:
            for j in notes[i]:
                for k in notes[i][j]:
                    print(j, k, notes[i][j][k])




def tasklist(path, c):
    if c == True:
        deadline = input("Enter the deadline for this task")
        task = input("Enter the task name")
        wrappers.add_task(path)
    if c == False:
        wrappers.read_notes(path, True, False)

def hangman():
    word_list = ['book', 'trophy', 'science', 'programming','python', 'mathematics', 'google', 'condition','power', 'water', 'studio', 'deploy']
    current_word = random.choice(word_list)
    print("Enter a letter")
    guesses = []
    turnsLeft = 10 
    while turnsLeft > 0:
        guessedCorrect = 0
        for char in current_word:
            if char in guesses:
                print(char, end=" ")
                guessedCorrect += 1
            elif char.lower() in ['a', 'e', 'i', 'o', 'u']:
                print(char, end = " ")
                guessedCorrect += 1
            else:
                print("_", end=" ")
        print()
        if guessedCorrect == len(current_word):
            print("You guessed it correctly, the word was", current_word)
            break
        guess = input("Make your guess: ")
        if guess.lower() not in ['a', 'e', 'i', 'o', 'u']:
            guesses.append(guess)
        else:
            continue

        if guess not in current_word:
            turnsLeft -= 1
            print("Wrong")
            print("You have", turnsLeft, " more guesses")
            print()
    else:
        print("You lost! The word was", current_word)
