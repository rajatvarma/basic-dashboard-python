import time
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "no", "No"]
required = ("\nUse only A, B, or C\n")
def intro():
    stone = int()
    blades = int()
    print("You wake up in the middle of the forest, not remembering anything."
          "Looking around, you realise that you were lying in front of a "
          "small hut, with a path leading away from it and there are nothing "
          "but trees around. There is an eerie silence to the forest, and you "
          "feel like you are being watched. Do you:")
    time.sleep(1)
    print("\nA. Explore the creepy hut"
          "\nB.Go down the dirt path"
          "\nC.Start crying")
    choice=input("->")
    if choice in answer_A:
        option_explorehut(stone, blades)
    elif choice in answer_B:
        option_dirtpath(stone, blades)
    elif choice in answer_C:
        print("\nWell, we cant do much now, can we.\n")
    else:
        print(required)
        intro()
def option_explorehut(stone, blades):
    print("\nYou decide to explore the strange, creepy hut. You open the door "
          "go inside. It is very dilapidated, with a few shelves in the corner "
          "and a table in the middle. Approaching the table, you see an odd "
          "looking stone. Do you pick it up?")
    time.sleep(1)
    choice=input("->")
    if choice in yes:
        stone=1
    else:
        stone=0
    print("\nA loud sound emerges in the corner, near the shelves. Do you check it out? ")
    time.sleep(1)
    choice=input("->")
    if choice in yes:
        print("\nYou see a pair of blades, that look unused and ancient looking. "
              "Do you grab them?")
        choice=input("->")
        if choice in yes:
            blades+=1
            option_dirtpath(stone, blades)
        else:
            blades=0
            option_dirtpath(stone, blades)
    else:
        option_dirtpath(stone, blades)
def option_dirtpath(stone, blades):
    print("\nYou set down on the dirt path, wary of the dense trees and "
          "shrubs surrounding it. You walk for some time, and come "
          "across a small clearing. It's an unnervingly beautiful sight, "
          "where you can see a lone pedestal in the centre, and vines "
          "that came out of the ground and curved around it. As you are "
          "about to approach it, a snarl comes from behind you and you "
          "see a horrific creature, and its head is glowing in the centre "
          "making its way towards you. Do you:")
    time.sleep(1)
    print("\nA. Run"
          "\nB. Lie down and start crying")
    choice=input("->")
    if choice in answer_A:
        option_run(stone, blades)
    elif choice in answer_C:
        print("\nI mean, you basically decided to lie down and start "
              "crying as the creature rushes to you. \n\nYou died!")
    else:
        print(required)
        option_dirtpath()
def option_run(stone, blades):
    print("\nYou start running away from the creature and towards the pedestal. "
          "You notice a small depression on the surface of the pedestal, "
          "roughly the size of a stone. Do you:")
    time.sleep(1)
    if stone>0 and blades>0:
        print("\nA. Place stone in pedestal"
              "\nB. Fight the creature"
              "\nC. Freeze")
        choice=input("->")
        if choice in answer_A:
            option_pedestal(stone, blades)
        elif choice in answer_B:
            option_fight(stone, blades)
        elif choice in answer_C:
            print("\nSeriously. There's a monster charging at you and you "
                  "decide to freeze. \n\nYou died!")
        else:
            print(required)
            option_run(stone, blades)
    else:
        print("\nYou look at the creature again and find out the bright glowing object "
              "on their head is a stone. You somehow need to acquire it. You "
              "have no choice but to fight the creature.")
        option_fight(stone, blades)
def option_fight(stone, blades):
    if blades>0:
        print("\nYou face the creature, the object on its head glowing bright. "
              "You draw out your twin blades. You both charge at each other and "
              "you strike the creature in torso with both blades. The creature "
              "dies. You pick up the stone that fell from its head, and walk to "
              "the pedestal")
        stone=1
        option_pedestal(stone, blades)
    else:
        print("\nYou are weaponless, but hold your ground. Do you charge towards "
              "creature?")
        time.sleep(1)
        choice=input("->")
        if choice in yes:
            print("\nYou charge at the creature, but it launches at you. \n\n You died!")
        else:
            print("\nYou stay where you are, and the creature charges at you. "
                  "Just as it comes to hit you, you sidestep and jump on it and "
                  "grab the stone. The creature dissapears immediately. You walk "
                  " towards the pedestal.")
            stone=1
            option_pedestal(stone, blades)
def option_pedestal(stone, blades):
    if stone>0:
        print("You place the stone on the pedestal. And immediately all you see is black.")
        time.sleep(1)
        print("You wake up in your bed, safe and sound. It was all a dream!")

intro()