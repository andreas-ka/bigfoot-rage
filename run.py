""" Import libraries used in the game """
import random
import time
import sys
from termcolor import cprint
import images #contains all ASCII arts used in game


run_wolf = [1, 2, 3]
loot_weapons = []
loot_map = []

game_over_message = [
    "GAME OVER! You aint no survivor man from Discovery channel!",
    "GAME OVER!, You swimming with the fishes now pal",
    "GAME OVER!, Your six feet under now dude",
    "GAME OVER!, You wished now you joined the boy scouts right? you dead",
    "GAME OVER!, That's the end of the road for you, better luck next time!",
    "GAME OVER!, Dear diary, today I died.",
    "GAME OVER!, Mistakes were made...",
    "GAME OVER!, I will have to call you back cause I'm dead!",
    "GAME OVER!, I'm the grim reaper and you're my next customer",
    "GAME OVER!, You have died of dysentery",
    "GAME OVER!, it's time to kick ass and chew bubble gum, oh wait I'm dead!",
    "GAME OVER!, Abort mission, I'm going for a nap for a very long time!"
]

def main():
    """ Starts the game and all the functions """
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


def display_intro():
    """The welcoming section, lets you choose your name, have to be alphabetical,
    using termcolor for a more alive feel.
    Running a while loop with isalpha to check if the input is alphabetical"""
    cprint(images.logo_img, 'red')
    cprint("----------- Made By: Andreas Karlsson 2023 ------------\n", 'yellow')
    print("Welcome to the text based adventure game that is Bigfoot Rage!")
    print("Can you make it out of the forest alive?\n")
    cprint("Game information:\n", 'yellow')
    print("1. Navigate the forest using printed options")
    print("2. Find loot to help you progress throughout the game")
    print("3. You may discover an Easter egg if you successfully gather all of the loot!")
    print("4. Last but not least SURVIVE!\n")
    print("What's you name fellow traveller?\n")
    username = ""
    loot_map.clear()
    loot_weapons.clear()
    while True:
        username = input("")
        if not username.isalpha():
            print("Sorry username have to be alphabetical")
            continue
        else:
            sys.stdout.write("\033[F")
            cprint("Welcome to the spooky forest ", 'red', end='')
            cprint(username, 'yellow', attrs=["bold"])
            print("\n")
            start_game_tile_one()


def start_game_tile_one():
    """Start of the game, Tile 1, the first part of the story.
    The user will be prompted to choose between 3 options
    depending on the choice, a different outcome.
    Checks the selected option to the start_game_options list; if not in the list it
    ask you to pick again.
    If option 3 then add 1 to loot_map, if loot_map = 1,2,3 then display suprise tile, if
    1 already in map_loot show that you already have it."""
    start_game_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in start_game_options:
        cprint("========================= INTRO =========================", 'green')
        print("You suddenly wake up, all confused and don't know where you are,")
        print("when you poke your head out of the tent all you see is dense")
        print("thick forest surrounding you, the tent only contains a blanket")
        print("and all your possessions are gone, wind is blowing and its really")
        print("cold out there. You are anxious and shaken, what is your next step?\n")
        print("1. You decide that best action is to stay in the tent, waiting for help")
        print("2. You find courage and try your luck walking straight into the forest")
        print("3. Search the area around the tent \n")
        user_choice = str(input("Which option do you pick 1,2 or 3? \n"))
        if user_choice == start_game_options[0]:
            cprint(random.choice(game_over_message),'red')
            cprint(images.dead_img, 'red')
            game_over()
        elif user_choice == start_game_options[1]:
            print("You decide to try your luck in the forest...")
            crossroad_tile_two()
        elif user_choice == start_game_options[2]:
            i = 1
            if i in loot_map:
                print("You have already collected the map piece")
                time.sleep(2)
                start_game_tile_one()
            else:
                cprint("Not much to find, until you notice a small piece", 'yellow')
                cprint("of paper that seems to be part of a map", 'yellow')
                loot_map.append(1)
                time.sleep(5)
                value = len(loot_map)
                if value == 3:
                    cprint("Let's combine them and see what it tells...", 'yellow')
                    time.sleep(2)
                    cprint("While in meadow maybe try option 5", 'magenta')
                    time.sleep(5)
                    start_game_tile_one()
                else:
                    cprint("Let's continue and head into the forest", 'yellow')
                    time.sleep(3)
                    crossroad_tile_two()
        else:
            print("Please pick 1, 2 or 3")


def crossroad_tile_two():
    """Crossroads Tile 2, Here the user will be greeted with three options.
    A while loop checks to see if the users choice is in the crossroad_options list
    if input that function will take place.
    The user must input to move along.
    Also, an if statement to check if the user has already killed the wolf; if so option blocked"""
    crossroad_options = ["1","2","3","4"]
    user_choice = ""
    while user_choice not in crossroad_options:
        cprint(images.dead_tree_img, 'green')
        cprint("========================= CROSSROADS =========================", 'green')
        print("Right in front of you is a crossroad, to the left you see a")
        print("light shining through the trees.")
        print("Straight ahead there are only trees and to the right there's a cave.")
        print("What option will go for?\n")
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
    """First tile in the game where the user can loot an item.
    If the user selects option 1, the user finds a knife, and appends the knife to the loot list.
    If the user already has the knife, you have to select a new option.
    While loop to check if selected option is in list cabin_options"""
    cabin_options = ["1","2"]
    user_choice = ""
    while user_choice not in cabin_options:
        cprint(images.cabin_img, 'yellow')
        cprint("========================= THE CABIN =========================", 'yellow')
        print("When you arrive at the source of the lights there is a clearing")
        print("and in the middle is a creepy looking cabin,")
        print("you don't see any movement inside and its all quiet, what will you do?\n")
        print("1. Search the cabin and hope for the best...")
        print("2. Way to scary, i better head back...\n")
        user_choice = input("Which option do you pick 1 or 2 ")
        if user_choice == cabin_options[0]:
            i = 1
            if i in loot_weapons:
                print("Seems you have already searched the cabin and found a knife")
                time.sleep(2)
                cabin_tile_three()
            else:
                print("You search the cabin even though you shiver in fear,")
                print("and in the back you find...")
                cprint("Holy moly a knife, that could be useful...", 'yellow')
                cprint("Let's go back to the crossroad...", 'yellow')
                loot_weapons.append(1)
                time.sleep(3)
                crossroad_tile_two()
        elif user_choice == cabin_options[1]:
            print("You turn around and head back to the crossroad")
            crossroad_tile_two()
        else:
            print("Please pick 1 or 2")


def wolf_den_tile_four():
    """User encounters the wolf, have to make the call if the user wants to fight or run!
    If a user tries to use his fists, it's game over, use the knife, and you kill the wolf.
    If the user selects the run option, there is a 66% chance random() of making it
    Check whether the user has the knife; if not, choose a new option.
    If the user kills the wolf with knife, it gets a piece of the map, append loot_map.
    And if the user already has the other two maps user get the message about the easter egg.
    If user already have loot_map 2 then you cant access wolf_den from crossroads."""
    wolf_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in wolf_options:
        cprint(images.wolf_img, 'grey')
        cprint("======================= WOLF DEN =======================", 'light_grey')
        print("In the darkness of the cave you suddenly hears a big roar!!")
        print("A big wolf appears and wants you for its dinner!")
        print("Now is the time to be brave and smart, what will you do?\n")
        print("1. I tackle the wolf head on with my fists!")
        print("2. I didn't have my cereals this morning I took my chances and made a RUN for it")
        print("3. Wait a minute, i have a knife, AAATTTAAACCKK!!\n")
        user_choice = input("Which option do you pick 1, 2 or 3? ")
        if user_choice == wolf_options[0]:
            cprint(random.choice(game_over_message),'red')
            cprint(images.dead_img, 'red')
            game_over()
        elif user_choice == wolf_options[1]:
            print("Like Usain Bolt you run for you life, did you make it?")
            run_chance = random.choice(run_wolf)
            time.sleep(2)
            if run_chance == 1:
                cprint("You got away safely, well done!!\n", 'green')
                print("back to crossroad...")
                time.sleep(3)
                crossroad_tile_two()
            elif run_chance == 2:
                cprint("Ouch! You are severely injured but managed to escape", 'green')
                cprint("back to the crossroad...\n", 'green')
                time.sleep(3)
                crossroad_tile_two()
            elif run_chance == 3:
                cprint(random.choice(game_over_message),'red')
                cprint(images.dead_img, 'red')
                time.sleep(4)
                game_over()
        elif user_choice == wolf_options[2]:
            i = 1
            if i in loot_weapons:
                cprint("You used you knife like Steven Seagal and with ease", 'green')
                cprint("the wolf is now dead phew...", 'green')
                time.sleep(2)
                cprint("On the the cave wall you find a piece of a map!", 'yellow')
                loot_map.append(2)
                time.sleep(3)
                value = len(loot_map)
                if value == 3:
                    cprint("Let's combine them and see what it tells...", 'yellow')
                    time.sleep(2)
                    cprint("While in meadow maybe try option 5", 'magenta')
                    time.sleep(5)
                    crossroad_tile_two()
                else:
                    cprint("Let's continue our exploration.", 'yellow')
                    time.sleep(3)
                    crossroad_tile_two()
            else:
                print("Hmm you dont seem to have a knife....\n")
                time.sleep(2)
                wolf_den_tile_four()
        else: print("Pretty please pick 1, 2 or 3")


def meadow_tile_five():
    """User reaches a meadow that also is a crossroad with three options,
    the 4th option is only known if the user has collected all three map pieces.
    Displays an ASCII art of a flower
    Same while loop to check if the option is in the meadow_options list"""
    cprint(images.flowers_img, 'magenta')
    meadow_options = ["1","2","3","4","5"]
    user_choice = ""
    while user_choice not in meadow_options:
        cprint("========================= MEADOW =========================", 'magenta')
        print("You clear the forest and come up to a big meadow filled with flowers,")
        print("far off in the distance to left you see a treehouse,")
        print("if you look right you can see the ocean, there's also some sort")
        print("of tree structure ahead of the meadow in the forest. ")
        print("What's your plan of action? \n")
        print("1. That treehouse looks cool, lets check it out ")
        print("2. Could use some ocean air right now, lets go there")
        print("3. What a strange structure, i need to check it out!")
        print("4. I think i have forgotten something, lets go to crossroads again...\n")
        user_choice = str(input("Which option do you pick 1, 2, 3 or 4? \n"))
        if user_choice == meadow_options[0]:
            print("You choose the path to the treehouse")
            treehouse_tile_six()
        elif user_choice == meadow_options[1]:
            print("You chose to head to the ocean...")
            ocean_tile_eight()
        elif user_choice == meadow_options[2]:
            i = 3
            if i in loot_weapons:
                print("You have already killed the bigfoot, choose another option...")
                time.sleep(2)
                meadow_tile_five()
            else:
                print("You chose to continue walking straight towards the structure...")
                bigfoot_tile_seven()
        elif user_choice == meadow_options[3]:
            print("Back to crossroads it is...")
            time.sleep(2)
            crossroad_tile_two()
        elif user_choice == meadow_options[4]:
            cprint("Wow what is this...")
            time.sleep(3)
            surprise_tile_ten()
        else:
            print("Please pick 1, 2, 3 or 4")


def treehouse_tile_six():
    """User gets to the treehouse if the user wants to climb up the user loot list append pistol,
    if they already have the pistol = choose another option.
    stay the night = game over.
    Same while loop to check if option is in the treehouse_options list"""
    cprint(images.treehouse_img, 'green')
    treehouse_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in treehouse_options:
        cprint("========================= TREEHOUSE =========================", 'green')
        print("Far up in the trees you see a treehouse, must be atleast")
        print("40 years old accordning to the state of it.")
        print("What will you do? \n")
        print("1. I want to see whats up there, lets climb it!")
        print("2. Nah that dosent look safe, i head back")
        print("3. Oh the perfect spot to the spend the night\n")
        user_choice = str(input("Which option do you pick 1, 2 or 3? \n"))
        if user_choice == treehouse_options[0]:
            i = 2
            if i in loot_weapons:
                print("You have already searched the treehouse...")
                time.sleep(2)
                treehouse_tile_six()
            else:
                print("You climbed the treehouse and behold you found a...")
                time.sleep(2)
                cprint(images.pistol_img, 'yellow')
                cprint("PISTOL!!! That will be handy further on...", 'yellow')
                cprint("Let's head back to the meadow...", 'yellow')
                loot_weapons.append(2)
                time.sleep(3)
                meadow_tile_five()
        elif user_choice == treehouse_options[1]:
            print("You head back to the meadow...")
            meadow_tile_five()
        elif user_choice == treehouse_options[2]:
            time.sleep(1)
            cprint(random.choice(game_over_message),'red')
            cprint(images.dead_img, 'red')
            time.sleep(3)
            game_over()
        else:
            print("Please pick 1, 2 or 3")


def bigfoot_tile_seven():
    """The big fight with the big guy. Here user only survives if they have acquired the pistol,
    When choosing option 4, it will check if the pistol is in the loot_weapon list; 
    if you do not have it, you will need to make a new choice.
    All other options = game over.
    Same while loop to check if the option is in the bigfoot_options list"""
    cprint(images.bigfoot_img, 'red')
    bigfoot_options = ["1","2","3","4"]
    user_choice = ""
    while user_choice not in bigfoot_options:
        cprint("========================= BIGFOOT =========================", 'red')
        print("You enter the big tree structure at the end of the meadow")
        print("you are now standing face to face with a huge angry bigfoot")
        print("who plans to have you as a snack.")
        print("What will you do?\n")
        print("1. You know what, i will finish him with my bare FISTS!")
        print("2. Hell no, not today mr bigfoot! RUUUN!")
        print("3. Wait i can use my knife! AAATTAACCKKK!")
        print("4. HAH time to taste lead big guy. I shoot my pistol!! ")
        user_choice = str(input("Which option do you pick 1, 2, 3 or 4? \n"))
        if user_choice == bigfoot_options[0]:
            time.sleep(1)
            cprint(random.choice(game_over_message),'red')
            cprint(images.dead_img, 'red')
            time.sleep(3)
            game_over()
        elif user_choice == bigfoot_options[1]:
            time.sleep(1)
            cprint(random.choice(game_over_message),'red')
            cprint(images.dead_img, 'red')
            time.sleep(3)
            game_over()
        elif user_choice == bigfoot_options[2]:
            i = 1
            if i in loot_weapons:
                cprint("You are gonna taste my fury big guy, I've got a knife!!", 'yellow')
                time.sleep(1)
                cprint(random.choice(game_over_message),'red')
                print(images.dead_img, 'red')
                game_over()
            else:
                print("Hmm you don't seem to have a knife....")
                time.sleep(1)
                bigfoot_tile_seven()
        elif user_choice == bigfoot_options[3]:
            i = 2
            if i in loot_weapons:
                print("You fire your pistol at the bigfoot...")
                time.sleep(2)
                cprint("The big guy makes one last growl while falling down to the ground", 'green')
                cprint("you did it!!!", 'green')
                cprint("Wait, he dropped something, i need to investigate...", 'green')
                time.sleep(1)
                cprint("Its a compass, should be useful! Lets continue...", 'yellow')
                loot_weapons.append(3)
                time.sleep(4)
                meadow_tile_five()
            else:
                print("Hmm you don't seem to have a pistol....\n")
                time.sleep(2)
                bigfoot_tile_seven()
        else:
            print("Please pick 1, 2, 3 or 4")


def ocean_tile_eight():
    """User gets to the ocean, the final tile of the game
    Using a raft without a compass in the loot list = game over.
    Use a raft and have the compass in the loot list = Success; you escaped!
    Option 3 gets you a map piece; choose another option if already in loot_map.
    Same while loop to check if the option is in the ocean_options list"""
    cprint(images.beach_img, 'cyan')
    ocean_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in ocean_options:
        cprint("========================= OCEAN =========================", 'cyan')
        print("There's a lovely breeze when you finally arrive at the ocean,")
        print("a long beautiful beach with white sand. and if you look ")
        print("far enough you spot a raft in the distance, could that be your salvation?")
        print("What will you do? \n")
        print("1. Yay i will try my luck with the raft!")
        print("2. Nah that doesn't look safe, i head back")
        print("3. Looks something is buried over there, maybe have a look...\n")
        user_choice = str(input("Which option do you pick 1, 2 or 3 \n"))
        if user_choice == ocean_options[0]:
            i = 3
            if i in loot_weapons:
                cprint("Like Columbus you set sail, and with the compass", 'green')
                cprint("at hand you find your way home \n", 'green')
                time.sleep(3)
                escape_tile_nine()
            else:
                print("Hmm you dont seem to have a compass....\n")
                time.sleep(2)
                cprint(random.choice(game_over_message),'red')
                cprint(images.dead_img, 'red')
                game_over()
        elif user_choice == ocean_options[1]:
            cprint("I head back and explore some more...", 'yellow')
            time.sleep(3)
            meadow_tile_five()
        elif user_choice == ocean_options[2]:
            i = 3
            if 3 in loot_map:
                print("Seems you have already searched there...")
                time.sleep(2)
                ocean_tile_eight()
            else:
                print("You start to dig with your bare hands, and find.....")
                time.sleep(2)
                cprint("another peice of a map", 'yellow')
                loot_map.append(3)
                time.sleep(3)
                value = len(loot_map)
                if value == 3:
                    cprint("Let's combine them and see what it tells...", 'yellow')
                    time.sleep(2)
                    cprint("While in meadow maybe try option 5", 'magenta')
                    time.sleep(5)
                    meadow_tile_five()
                else:
                    print("Let's continue this nightmare...")
                    time.sleep(2)
                    ocean_tile_eight()
        else:
            print("Please select 1,2 or 3")
            time.sleep(3)


def escape_tile_nine():
    """ This only shows if the user finishes the game,
    Congratulations to the user for completing the game!
    Users will be asked if they want to play again
    Same while loop to check if the option is in the escape_options list"""
    escape_options = ["y","n"]
    cprint(images.escaped_img, 'green')
    user_choice = ""
    while user_choice not in escape_options:
        cprint("======================= CONGRATULATIONS =======================", 'green')
        print("Well done on completing the game!")
        print("You are truly a survivor!\n")
        print("Want to play again? y/n \n")
        user_input = str(input("").lower())
        if user_input == "y":
            time.sleep(2)
            display_intro()
            loot_map.clear()
            loot_weapons.clear()
        elif user_input == "n":
            print("Thank you for playing the game!")
            time.sleep(4)
            quit()
        else:
            print("You can only type y for yes or n for no!")


def surprise_tile_ten():
    """ This tile is only available if the user collects all three pieces of the map
    Just a fun ascii image and well done"""
    cprint(images.surprise_img, 'blue')
    cprint("Well done! Just a little easter egg...", 'yellow')
    cprint("Cant hang around here, you still need to escape...", 'yellow')
    time.sleep(5)
    meadow_tile_five()


def game_over():
    """ Runs whenever the user dies, displays a random death quote
    from the game_over_message list, and an ASCII death art. 
    Lets user choose if they want to play again """
    cprint("======================== THANKS FOR PLAYING ========================", 'red')
    print("Want to play again? y/n \n")
    user_input = str(input("").lower())
    if user_input == "y":
        time.sleep(2)
        display_intro()
        loot_map.clear()
        loot_weapons.clear()
    elif user_input == "n":
        print("Thank you for playing the game!")
        time.sleep(4)
        quit()
    else:
        print("You can only type y for yes or n for no!")

main()
