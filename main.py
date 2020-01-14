import actions
import wrappers
import os

dashboard_name = "Epic"

cwd = os.getcwd()
info_dir = cwd+'\prfiles'

print("Welcome to", dashboard_name, "Dashboard, your one program for all daily tasks.")
print("Please wait while we set things up...")
print("What would you like to do today?")

while True:
    print("1. Check the weather")
    print("2. Get the most important headlines")
    print("3. Make some notes")
    print("4. Play Hangman")
    print("5. Exit this program")

    user_action_choice = input("Enter the option number: ")
    try:
        user_action_choice =  int(user_action_choice)
        if user_action_choice == 1:
            print("Please wait while results are fetched...")
            response = actions.weather()
            for i in response:
                if i == "Humidity":
                    print(i + " : " + str(response[i])+"%")
                else:
                    print(i + " : " + str(response[i])+"°C")
        elif user_action_choice == 2:
            keyword = input("Enter a keyword for the search: ")
            print("Please wait while results are fetched...")
            response = actions.news(keyword)
            if type(response) == str:
                print(response)
            else:
                for i in response:
                    print(i[0], i[1])
        elif user_action_choice == 3:
            r_or_c = input("Press 1 to read existing notes or press 2 to create a new note")
            if r_or_c == "1":
                actions.notes(info_dir, c=True)
            elif r_or_c == "2":
                actions.notes(info_dir, c=False)
        elif user_action_choice == 4:
            actions.hangman()
        elif user_action_choice == 5:
            print("Come back soon!")
            break
    except:
        print("Oh no! We asked you for the option number, but you gave us", user_action_choice, "! Try again with the option number.")
