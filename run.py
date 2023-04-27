import random
import termcolor
import images
import time

run_wolf = [1, 2, 3]

def main():
    display_intro()
    #user_name = display_intro()
    start_game_tile_one()
    crossroad_tile_two()
    cabin_tile_three()


"""Classes for character and enemies"""
class Character:
    def __init__(self, name, health, strength):
        Character.name = user_name
        Character.health = health
        Character.strength = strength


class Wolf:
    def __init__(self, health, strength):
        Wolf.health = health
        Wolf.strength = strength


class Bigfoot:
    def __init__(self, health, strength):
        Bigfoot.health = health
        Bigfoot.strength = strength


class Loot:
    def __init__(self, strength, health):
        Loot.strength = strength
        Loot.health = health


def display_intro():
    """The welcoming section, let's you choose your name."""
    termcolor.cprint(images.logo_img, 'red')
    print("Welcome to the text based adventure game that is Bigfoot Rage!")
    print("Can you make it out of the forrest alive?\n")
    print("What's you name fellow traveller?")
    username = ""
    while True:
        username = input("")
        if not username.isalpha():
            print("Sorry username have to be alphabetical")
            continue
        else:
            print("Welcome to the spooky forest " + username + "\n")
            start_game_tile_one()
            

def start_game_tile_one():
    """Start of the game, Tile 1, first part of the story."""
    print("You suddenly wake up, all confused and don't know where you are,")
    print("when you poke your head out of the tent all you see is dense thick forest surrounding you,")
    print("the tent only contains a blanket and all your possesions are gone, wind is blowing and its really cold out there.")
    print("You are anxoius and shaken, what is your next step\n")
    print("1. You descide that best action is to stay inte the tent, waiting for help")
    print("2. You find courage and try luck walking straight into the forest \n")
    option = ""
    while option != "1" and option != "2":
        option = input("Which option do you pick 1 or 2? \n")
        print("\n")
        if option == "1":
            print("What were you thinking, you have freezed to death!")
            termcolor.cprint(images.dead_img, 'red')
            quit()
        elif option == "2":
            print("You decide to try your luck in the forest...")
            crossroad_tile_two()
        else:
            print("Please pick 1 or 2")
            break


def crossroad_tile_two():
    """Crossroads Tile 2, Here the user will be greeted with 3 options."""
    termcolor.cprint(images.dead_tree_img, 'green')
    print("Right infront of you is a crossroad, you peak to left and see a light shining through the trees,")
    print("straight ahead theres only trees and to the right theres a cave. What option will go for?\n")
    print("1. Go left and see what the lights are coming from")
    print("2. I want to explore the cave to the right")
    print("3. Continue on the straight path\n")
    option = input("Which option do you pick 1, 2 or 3? ")
    if option == "1":
        print("You chose to go towards the lights...")
        cabin_tile_three()
    elif option == "2":
        print("You chose to head to the cave...")
        wolf_den_tile_four()
    elif option == "3":
        print("You chose to continue walking straight...")
        meadow_tile_five()
    else:
        print("Please pick 1, 2 or 3")
        

def cabin_tile_three():
    """First tile in the game where the user is able to loot an item."""
    termcolor.cprint(images.cabin_img, 'yellow')
    print("When you arrive at the source of the lights there is a clearing and in the middle is a creepy looking cabin,")
    print("you dont see any movement inside and its all quiet, what will you do?\n")
    print("1. Search the cabin and hope for the best...")
    print("2. Way to scary, i better head back...\n")
    option = input("Which option do you pick 1 or 2 ")
    if option == "1":
        print("You search the cabin even though you shiver in fear, and in the back you find...")
        termcolor.cprint("Holy moly a knife, that could be useful", 'yellow')
        time.sleep(5)
        crossroad_tile_two()
    elif option == "2":
        print("You turn around and head back to the crossroad")
        crossroad_tile_two()
    else:
        print("Please pick 1 or 2")


def wolf_den_tile_four():
    """User encounters the wolf, have to make the call if user wants to fight or run!"""
    termcolor.cprint(images.wolf_img, 'grey')
    print("In the darkness of the cave you suddenly hears a big roar!! A big wolf appears and wants you for its dinner!")
    print("Now is the time to be brave and smart, what will you do?\n")
    print("1. I tackle the wolf head on with my fists!")
    print("2. I didnt have my cereals this morning i take my chances and make a RUN for it!!!")
    print("3. Wait a minute, i have a knife, AAATTTAAACCKK!!\n")
    option = input("Which option do you pick 1, 2 or 3? ")
    if option == "1":
        print("Not even Chuck Norris can kill a wolf with his fists, you died!!!")
        termcolor.cprint(images.dead_img, 'red')
        quit()
    elif option == "2":
        print("Like Usain Bolt you run for you life, did you make it?")
        run_chance = random.choice(run_wolf)
        if run_chance == 1:
            print("You got away safely, well done!!\n")
            print("back to crossroad...")
            time.sleep(4)
            crossroad_tile_two()
        elif run_chance == 2:
            print("Ouch! You are severly injured but managed to escape back to crossroad...\n")
            time.sleep(4)
            crossroad_tile_two()
        else:
            run_chance == 3
            print("Not even Usain Bolt can outrun a wolf silly, you died!!")
            termcolor.cprint(images.dead_img, 'red')
            time.sleep(4)
            quit()
    elif option == "3":
        print("You used you knife like Steven Seagal and with ease the wolf is now dead pheew...back to the crossroad...\n")
        time.sleep(4)
        crossroad_tile_two()
    else:
        print("Please pick 1, 2 or 3")


main()
