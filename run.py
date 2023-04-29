import random
import termcolor
import images
import time
import sys


""" List used in the game """
run_wolf = [1, 2, 3]

loot_weapons = []
loot_map = [1,2]

game_over_message = [
    "GAME OVER! You aint no survivor man from discover channel!",
    "GAME OVER!, You swimming with the fishes now pal",
    "GAME OVER!, Your six feet under now dude",
    "GAME OVER!, You wished now you joined the boyscouts right? you dead",
    "GAME OVER!, Thats the end of the road for you, better luck next time!",
    "GAME OVER!, Dear diary, today I died.",
    "GAME OVER!, Mistakes were made...",
    "GAME OVER!, I will have to call you back cause im dead!",
    "GAME OVER!, I'm the grim reaper and you're my next customer",
    "GAME OVER!, You have died of dysentery",
    "GAME OVER!, it's time to kick ass and chew bubble gum, oh wait im dead!",
    "GAME OVER!, Abort mission, im goin for a nap for a very long time!"
]


def main():
    display_intro()
    start_game_tile_one()
    crossroad_tile_two()
    cabin_tile_three()
    wolf_den_tile_four()
    meadow_tile_five()
    treehouse_tile_six()
    bigfoot_tile_seven()
    ocean_tile_eight()
    escape_tile_nine()
    game_over()
    surprise_tile_ten()


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
    """The welcoming section, let's you choose your name, have to be alphabetical"""
    termcolor.cprint(images.logo_img, 'red')
    termcolor.cprint("----------- Made By: Andreas Karlsson 2023 ------------\n", 'yellow')
    print("Welcome to the text based adventure game that is Bigfoot Rage!")
    print("Can you make it out of the forest alive?\n")
    termcolor.cprint("Game information:\n", 'yellow')
    print("1. Navigate the forest using printed options")
    print("2. Find loot to help you progress trough out the game")
    print("3. Last but not least SURVIVE!\n")
    print("What's you name fellow traveller?\n")
    username = ""
    while True:
        username = input("")
        if not username.isalpha():
            print("Sorry username have to be alphabetical")
            continue
        else:
            sys.stdout.write("\033[F")
            termcolor.cprint("Welcome to the spooky forest ", 'red', end='')
            termcolor.cprint(username, 'yellow', attrs=["bold"])
            print("\n")
            start_game_tile_one()
            
            
def start_game_tile_one():
    """Start of the game, Tile 1, first part of the story.
    User will be prompted to make a choice between 2 options
    depending on choice a different outcome"""
    start_game_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in start_game_options:
        termcolor.cprint("========================= INTRO =========================", 'green')
        print("You suddenly wake up, all confused and don't know where you are,")
        print("when you poke your head out of the tent all you see is dense")
        print("thick forest surrounding you, the tent only contains a blanket")
        print("and all your possesions are gone, wind is blowing and its really")
        print("cold out there. You are anxoius and shaken, what is your next step?\n")
        print("1. You descide that best action is to stay inte the tent, waiting for help")
        print("2. You find courage and try luck walking straight into the forest")
        print("3. Search the area around the tent \n")
        user_choice = str(input("Which option do you pick 1,2 or 3? \n"))

        if user_choice == start_game_options[0]:
            termcolor.cprint(random.choice(game_over_message),'red')
            termcolor.cprint(images.dead_img, 'red')
            game_over()
        elif user_choice == start_game_options[1]:
            print("You decide to try your luck in the forest...")
            crossroad_tile_two()
        elif user_choice == start_game_options[2]:
            termcolor.cprint("Not much to find, until you notice a small piece of paper that seems", 'yellow')
            termcolor.cprint("to be part of a bigger map, let's hope you find the rest", 'yellow')
            loot_map.append(1)
            time.sleep(5)
            values = [1,2,3]
            if values == loot_map:
                termcolor.cprint("Let's combine them and see what it tells...", 'yellow')
                time.sleep(2)
                termcolor.cprint("While in meadow maybe try option 4", 'yellow')
                time.sleep(5)
            else:
                termcolor.cprint("Let's countinue our exploration and head into the forest", 'yellow')
                time.sleep(3)
                crossroad_tile_two()
        else:
            print("Please pick 1, 2 or 3")
            

def crossroad_tile_two():
    """Crossroads Tile 2, Here the user will be greeted with 3 options.
    A while loop checks to see if users choice is in the crossroad_options list
    if input that function will take place.
    User must do an input to move along"""
    crossroad_options = ["1","2","3","4"]
    user_choice = ""
    while user_choice not in crossroad_options:
        termcolor.cprint(images.dead_tree_img, 'green')
        termcolor.cprint("========================= CROSSROADS =========================", 'green')
        print("Right infront of you is a crossroad, you peak to left and see a light shining through the trees,")
        print("straight ahead theres only trees and to the right theres a cave. What option will go for?\n")
        print("1. Go left and see what the lights are coming from")
        print("2. I want to explore the cave to the right")
        print("3. Continue on the straight path")
        print("4. I dont like this at all, lets return to the tent\n")
   
        user_choice = str(input("Which option do you pick 1, 2, 3 or 4? "))
        if user_choice == crossroad_options[0]:
            print("You chose to go towards the lights...")
            cabin_tile_three()
        elif user_choice == crossroad_options[1]:
            i = 2
            if i in loot_map:
                print("You have already killed the wolf..")
                time.sleep(2)
                crossroad_tile_two()
            else:
             print("You chose to head to the cave...")
             wolf_den_tile_four()
        elif user_choice == crossroad_options[2]:
            print("You chose to continue walking straight...")
            meadow_tile_five()
        elif user_choice == crossroad_options[3]:
            print("You chose to head back to the tent...")
            start_game_tile_one()
    else:
        print("Please pick 1, 2, 3 or 4")
        

def cabin_tile_three():
    """First tile in the game where the user is able to loot an item.
    If user selects option 1 the user finds a knife, append the knife to loot list"""
    cabin_options = ["1","2"]
    user_choice = ""
    while user_choice not in cabin_options:
        termcolor.cprint(images.cabin_img, 'yellow')
        termcolor.cprint("========================= THE CABIN =========================", 'yellow')
        print("When you arrive at the source of the lights there is a clearing and in the middle is a creepy looking cabin,")
        print("you dont see any movement inside and its all quiet, what will you do?\n")
        print("1. Search the cabin and hope for the best...")
        print("2. Way to scary, i better head back...\n")
        user_choice = input("Which option do you pick 1 or 2 ")
        if user_choice == cabin_options[0]:
            i = 1
            for i in loot_weapons:
                print("Seems you have already searched the cabin and found a knife")
                time.sleep(2)
                cabin_tile_three()
            else:
                print("You search the cabin even though you shiver in fear, and in the back you find...")
                termcolor.cprint("Holy moly a knife, that could be useful, back to the crossroad...", 'yellow')
                loot_weapons.append(1)
                time.sleep(3)
                crossroad_tile_two()
        elif user_choice == cabin_options[1]:
            print("You turn around and head back to the crossroad")
            crossroad_tile_two()
        else:
            print("Please pick 1 or 2")


def wolf_den_tile_four():
    """User encounters the wolf, have to make the call if user wants to fight or run!
    If user tries to use his fists it's game over, use the knife and you kill the wolf.
    If the user selects the run option there is a 66% chance of making it"""
    wolf_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in wolf_options:
        termcolor.cprint(images.wolf_img, 'grey')
        termcolor.cprint("========================= WOLF DEN =========================", 'light_grey')
        print("In the darkness of the cave you suddenly hears a big roar!! A big wolf appears and wants you for its dinner!")
        print("Now is the time to be brave and smart, what will you do?\n")
        print("1. I tackle the wolf head on with my fists!")
        print("2. I didnt have my cereals this morning i take my chances and make a RUN for it!!!")
        print("3. Wait a minute, i have a knife, AAATTTAAACCKK!!\n")
        user_choice = input("Which option do you pick 1, 2 or 3? ")
        if user_choice == wolf_options[0]:
            termcolor.cprint(random.choice(game_over_message),'red')
            termcolor.cprint(images.dead_img, 'red')
            game_over()
        elif user_choice == wolf_options[1]:
            print("Like Usain Bolt you run for you life, did you make it?")
            run_chance = random.choice(run_wolf)
            time.sleep(2)
            if run_chance == 1:
                termcolor.cprint("You got away safely, well done!!\n", 'green')
                print("back to crossroad...")
                time.sleep(3)
                crossroad_tile_two()
            elif run_chance == 2:
                termcolor.cprint("Ouch! You are severly injured but managed to escape back to crossroad...\n", 'green')
                time.sleep(3)
                crossroad_tile_two()
            else:
                run_chance == 3
                termcolor.cprint(random.choice(game_over_message),'red')
                termcolor.cprint(images.dead_img, 'red')
                time.sleep(4)
                game_over()
        elif user_choice == wolf_options[2]:
            i = 1
            for i in loot_weapons:
                termcolor.cprint("You used you knife like Steven Seagal and with ease", 'green')
                termcolor.cprint("the wolf is now dead pheew...", 'green')
                time.sleep(2)
                termcolor.cprint("On the the cave wall you find a piece of a map!", 'yellow')
                loot_map.append(2)
                time.sleep(5)
                values = [1,2,3]
                if values == loot_map:
                    termcolor.cprint("Let's combine them and see what it tells...", 'yellow')
                    time.sleep(2)
                    termcolor.cprint("While in meadow maybe try option 4", 'yellow')
                    time.sleep(5)
                else:
                    termcolor.cprint("Let's countinue our exploration.", 'yellow')
                    time.sleep(3)
                    crossroad_tile_two()
            else:
                print("Hmm you dont seem to have a knife....\n")
                time.sleep(2)
                wolf_den_tile_four()      
        else: print("Pretty please pick 1, 2 or 3")
            
        
def meadow_tile_five():
    """User reaches a meadow that also is a crossroad with 3 options
    Displays an ascii art om a flower"""
    termcolor.cprint(images.flowers_img, 'magenta')
    meadow_options = ["1","2","3","4"]
    user_choice = ""
    while user_choice not in meadow_options:
        termcolor.cprint("========================= MEADOW =========================", 'magenta')
        print("You clear the forest and come up to a big meadow filled with flowers, far off in the distance to left you see a treehouse,")
        print("if you look right you can see the ocean, theres also some sort of tree structure ahead of the meadow in the forest. ")
        print("Whats your plan of action? \n")
        print("1. That treehouse looks cool, lets check it out ")
        print("2. Could use some ocean air right now, lets go there")
        print("3. What a strange structure, i need to check it out!\n")
        user_choice = str(input("Which option do you pick 1, 2 or 3? \n"))
        if user_choice == meadow_options[0]:
            print("You choose the path to the treehouse")
            treehouse_tile_six()
        elif user_choice == meadow_options[1]:
            print("You chose to head to the ocean...")
            ocean_tile_eight()
        elif user_choice == meadow_options[2]:
            print("You chose to continue walking straight towards the structure...")
            bigfoot_tile_seven()
        elif user_choice == meadow_options[3]:
            termcolor.cprint("Wow what is this...")
            time.sleep(3)
            surprise_tile_ten()
    else:
        print("Please pick 1, 2 or 3")
        


def treehouse_tile_six():
    """User gets to the treehouse, if user wants climb up loot list append pistol,
    stay the night = game over."""
    termcolor.cprint(images.treehouse_img, 'green')
    treehouse_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in treehouse_options:
        termcolor.cprint("========================= TREEHOUSE =========================", 'green')
        print("Far up in the trees you see a treehouse, must be atleast 40 years old accordning to the state of it.")
        print("What will you do? \n")
        print("1. I want to see whats up there, lets get up there!")
        print("2. Nah that dosent look safe, i head back")
        print("3. Oh the perfect spot to the spend the night\n")
        user_choice = str(input("Which option do you pick 1, 2 or 3? \n"))
        print(loot_weapons)
        if user_choice == treehouse_options[0]:
            i = 2
            if i in loot_weapons:
                print("You have already searched the treehouse...")
                time.sleep(2)
                treehouse_tile_six()
            else:
                print("You climbed the treehouse and behold you found a...")
                time.sleep(2)
                termcolor.cprint(images.pistol_img, 'yellow')
                termcolor.cprint("PISTOL!!! That will be handy further on, back to the meadow...", 'yellow')
                loot_weapons.append(2)
                time.sleep(3)
                meadow_tile_five()
        elif user_choice == treehouse_options[1]:
            print("You head back to the meadow...")
            meadow_tile_five()
        elif user_choice == treehouse_options[2]:
            time.sleep(1)
            termcolor.cprint(random.choice(game_over_message),'red')
            termcolor.cprint(images.dead_img, 'red')
            time.sleep(3)
            game_over()
    else:
        print("Please pick 1, 2 or 3")


def bigfoot_tile_seven():
    """The big fight with the big guy. Here user only survives if they have aquired the pistol,
    when choosing option 4 it will check if pistol is in loot list,
    if you dont have the pistol you will need to make a new choice.
    all other options = game over."""
    termcolor.cprint(images.bigfoot_img, 'red')
    bigfoot_options = ["1","2","3","4"]
    user_choice = ""
    while user_choice not in bigfoot_options:
        termcolor.cprint("========================= BIGFOOT =========================", 'red')
        print("You enter the big tree structure at the end of the meadow, not your best life choice,")
        print("you are now standing face to face with a huge bigfoot who plans to have you as a snack.")
        print("What will you do?\n")
        print("1. You know what, i will finish him with my bare FISTS!")
        print("2. Hell no, not today mr bigfoot! RUUUN!")
        print("3. Wait i can use my knife! AAATTAACCKKK!")
        print("4. HAH time to taste lead big guy. I shoot my pistol!! ")
        user_choice = str(input("Which option do you pick 1, 2, 3 or 4? \n"))
        print(loot_weapons)
        if user_choice == bigfoot_options[0]:
            time.sleep(1)
            termcolor.cprint(random.choice(game_over_message),'red')
            termcolor.cprint(images.dead_img, 'red')
            time.sleep(3)
            game_over()
        elif user_choice == bigfoot_options[1]:
            time.sleep(1)
            termcolor.cprint(random.choice(game_over_message),'red')
            termcolor.cprint(images.dead_img, 'red')
            time.sleep(3)
            game_over()
        elif user_choice == bigfoot_options[2]:
            termcolor.cprint("You are gonna taste my fury big guy, ive got a knife!!", 'yellow')
            time.sleep(1)
            termcolor.cprint(random.choice(game_over_message),'red')
            termcolor.cprint(images.dead_img, 'red')
            game_over()
        elif user_choice == bigfoot_options[3]:
            i = 2
            for i in loot_weapons:
                print("You fire your pistol at the bigfoot...")
                time.sleep(2)
                termcolor.cprint("The big guy makes a last loud growl while falling down to the ground, you did it!!!", 'green')
                termcolor.cprint("Wait, he dropped something, i need to investigate...", 'green')
                time.sleep(1)
                termcolor.cprint("Its a compass, should be useful! Now back to the meadow...", 'yellow')
                loot_weapons.append(3)
                time.sleep(4)
                meadow_tile_five()
            else:
                print("Hmm you dont seem to have a pistol....\n")
                time.sleep(2)
                bigfoot_tile_seven()
    else:
        print("Please pick 1, 2, 3 or 4")


def ocean_tile_eight():
    """User gets to the ocean, the final tile of the game
    use raft without compass in loot list = game over.
    use raft and have the compass in loot list = Success, you escaped!"""
    termcolor.cprint(images.beach_img, 'cyan')
    ocean_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in ocean_options:
        termcolor.cprint("========================= OCEAN =========================", 'cyan')
        print("Theres a lovely breeze when you finally arrive at the ocean,")
        print("a long beautiful beach with white sand. and if you look ")
        print("far enough you spot a raft in the distance, could that be your salvation?")
        print("What will you do? \n")
        print("1. Yay i will try my luck with the raft!")
        print("2. Nah that dosent look safe, i head back")
        print("3. Looks something is buried over there, maybe have a look...\n")
        print(loot_map)
        user_choice = str(input("Which option do you pick 1, 2 or 3 \n"))
        if user_choice == ocean_options[0]:
            i = 3
            for i in loot_weapons:
                termcolor.cprint("Like Columbus you set sail, and with the compass at hand you find your way home \n", 'green')
                time.sleep(3)
                escape_tile_nine()
            else:
                print("Hmm you dont seem to have a compass....\n")
                time.sleep(2)
                termcolor.cprint(random.choice(game_over_message),'red')
                termcolor.cprint(images.dead_img, 'red')
                game_over()
        elif user_choice == ocean_options[1]:
            termcolor.cprint("I head back and explore some more...", 'yellow')
            time.sleep(3)
            meadow_tile_five()
        elif user_choice == ocean_options[2]:
            loot_values = [1,2,3]
            if loot_values == loot_map:
                print("Seems you have already searched there...")
                time.sleep(2)
                ocean_tile_eight()
            else:
                print("You start to dig with your bare hands, and find.....")
                time.sleep(2)
                termcolor.cprint("another peice of a map", 'yellow')
                loot_map.append(3)
                time.sleep(3)
                values = [1,2,3]
                if values == loot_map:
                    termcolor.cprint("Let's combine them and see what it tells...", 'yellow')
                    time.sleep(2)
                    termcolor.cprint("While in meadow maybe try option 4", 'yellow')
                    time.sleep(5)
                    meadow_tile_five()
        else:
            termcolor.cprint("Let's countinue our exploration and choose another option", 'yellow')
            time.sleep(3)
            ocean_tile_eight()


def escape_tile_nine():
    """ This only shows if user finish the game
    user will asked if they want to play again """
    termcolor.cprint(images.escaped_img, 'green')
    termcolor.cprint("========================= CONGRATULATIONS =========================", 'green')
    print("Well done on completing the game!")
    print("You are truly a survivor!\n")
    print("Want to play again? y/n \n")
    user_input = str(input(""))
    if user_input == "y":
        time.sleep(2)
        display_intro()
    elif user_input == "n":
        print("Thank you for playing the game!")
        time.sleep(4)
        quit()
    else:
        print("You can only type y for yes or n for no!")


def surprise_tile_ten():
    """ This tile is only available if user collects all three pieces of the map """
    termcolor.cprint(images.surprise_img, 'blue')
    termcolor.cprint("Well done! Just a little easter egg...", 'yellow')
    termcolor.cprint("Cant hang around here, you still need to escape...", 'yellow')
    time.sleep(5)
    meadow_tile_five()


def game_over():
    """ Runs whenever the user dies, lets you choose if you want to play again """
    termcolor.cprint("======================== THANKS FOR PLAYING ========================", 'red')
    print("Want to play again? y/n \n")
    user_input = str(input(""))
    if user_input == "y":
        time.sleep(2)
        display_intro()
    elif user_input == "n":
        print("Thank you for playing the game!")
        time.sleep(4)
        quit()
    else:
        print("You can only type y for yes or n for no!")


main()
