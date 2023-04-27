import random
import termcolor
import images
import time

run_wolf = [1, 2, 3]

loot = []

def main():
    display_intro()
    #user_name = display_intro()
    start_game_tile_one()
    crossroad_tile_two()
    cabin_tile_three()
    wolf_den_tile_four()
    meadow_tile_five()
    treehouse_tile_six()
    bigfoot_tile_seven()


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
            termcolor.cprint("Welcome to the spooky forest " + username + "\n", 'red')
            start_game_tile_one()
            
            
def start_game_tile_one():
    """Start of the game, Tile 1, first part of the story."""
    start_game_options = ["1","2"]
    user_choice = ""
    while user_choice not in start_game_options:
        print("You suddenly wake up, all confused and don't know where you are,")
        print("when you poke your head out of the tent all you see is dense thick forest surrounding you,")
        print("the tent only contains a blanket and all your possesions are gone, wind is blowing and its really cold out there.")
        print("You are anxoius and shaken, what is your next step\n")
        print("1. You descide that best action is to stay inte the tent, waiting for help")
        print("2. You find courage and try luck walking straight into the forest \n")
        user_choice = str(input("Which option do you pick 1 or 2? \n"))

        if user_choice == start_game_options[0]:
            print("What were you thinking, you have freezed to death!")
            termcolor.cprint(images.dead_img, 'red')
            quit()
        elif user_choice == start_game_options[1]:
            print("You decide to try your luck in the forest...")
            crossroad_tile_two()
        else:
            print("Please pick 1 or 2")
            

def crossroad_tile_two():
    """Crossroads Tile 2, Here the user will be greeted with 3 options."""
    crossroad_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in crossroad_options:
        termcolor.cprint(images.dead_tree_img, 'green')
        print("Right infront of you is a crossroad, you peak to left and see a light shining through the trees,")
        print("straight ahead theres only trees and to the right theres a cave. What option will go for?\n")
        print("1. Go left and see what the lights are coming from")
        print("2. I want to explore the cave to the right")
        print("3. Continue on the straight path\n")
   
        user_choice = str(input("Which option do you pick 1, 2 or 3? "))
        if user_choice == crossroad_options[0]:
            print("You chose to go towards the lights...")
            cabin_tile_three()
        elif user_choice == crossroad_options[1]:
            print("You chose to head to the cave...")
            wolf_den_tile_four()
        elif user_choice == crossroad_options[2]:
            print("You chose to continue walking straight...")
            meadow_tile_five()
    else:
        print("Please pick 1, 2 or 3")
        

def cabin_tile_three():
    """First tile in the game where the user is able to loot an item."""
    cabin_options = ["1","2"]
    user_choice = ""
    while user_choice not in cabin_options:
        termcolor.cprint(images.cabin_img, 'yellow')
        print("When you arrive at the source of the lights there is a clearing and in the middle is a creepy looking cabin,")
        print("you dont see any movement inside and its all quiet, what will you do?\n")
        print("1. Search the cabin and hope for the best...")
        print("2. Way to scary, i better head back...\n")
        user_choice = input("Which option do you pick 1 or 2 ")
        if user_choice == cabin_options[0]:
            print("You search the cabin even though you shiver in fear, and in the back you find...")
            termcolor.cprint("Holy moly a knife, that could be useful, back to the crossroad...", 'yellow')
            loot.append("knife")
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
        print("In the darkness of the cave you suddenly hears a big roar!! A big wolf appears and wants you for its dinner!")
        print("Now is the time to be brave and smart, what will you do?\n")
        print("1. I tackle the wolf head on with my fists!")
        print("2. I didnt have my cereals this morning i take my chances and make a RUN for it!!!")
        print("3. Wait a minute, i have a knife, AAATTTAAACCKK!!\n")
        user_choice = input("Which option do you pick 1, 2 or 3? ")
        if user_choice == wolf_options[0]:
            termcolor.cprint("Not even Chuck Norris can kill a wolf with his fists, you died!!!", 'red')
            termcolor.cprint(images.dead_img, 'red')
            quit()
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
                termcolor.cprint("Not even Usain Bolt can outrun a wolf silly, you died!!", 'red')
                termcolor.cprint(images.dead_img, 'red')
                time.sleep(4)
                quit()
        elif user_choice == wolf_options[2]:
            i = "knife"
            for i in loot:
                termcolor.cprint("You used you knife like Steven Seagal and with ease the wolf is now dead pheew...back to the crossroad...\n", 'green')
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
    meadow_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in meadow_options:
        print("You clear the forest and come up to a big meadow filled with flowers, far off in the distance to left you see a treehouse,")
        print("if you look right you can see the ocean, theres also some sort of tree structure ahead of the meadow in the forest. ")
        print("Whats your plan of action? \n")
        print("1. That treehouse looks cool, lets check it out ")
        print("2. Could use some ocean air right now, lets go there")
        print("3. What a strang structure, i need to check it out!\n")
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
    else:
        print("Please pick 1, 2 or 3")


def treehouse_tile_six():
    """User gets to the treehouse, if user wants climb up loot = pistol,
    stay the night = game over."""
    termcolor.cprint(images.treehouse_img, 'grey')
    treehouse_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in treehouse_options:
        print("Far up in the trees you see a treehouse, must be atleast 20 years old accordning to the state of it.")
        print("What will you do? \n")
        print("1. I want to see whats up there, lets climb")
        print("2. Nah that dosent look safe, i head back")
        print("3. Oh the perfect spot to the spend the night")
        user_choice = str(input("Which option do you pick 1, 2 or 3? \n"))
        if user_choice == treehouse_options[0]:
            print("You climbed the treehouse and behold you found a:")
            time.sleep(2)
            termcolor.cprint(images.pistol_img, 'yellow')
            termcolor.cprint("PISTOL!!! That will be handy further on, back to meadow...", 'yellow')
            loot.append("pistol")
            time.sleep(3)
            meadow_tile_five()
        elif user_choice == treehouse_options[1]:
            print("You head back to the meadow...")
            meadow_tile_five()
        elif user_choice == treehouse_options[2]:
            print("This will be kinda cozy!")
            time.sleep(1)
            termcolor.cprint("You freezed to death, not so cozy anymore hah!", 'red')
            termcolor.cprint(images.dead_img, 'red')
            time.sleep(3)
            quit()
    else:
        print("Please pick 1, 2 or 3")

def bigfoot_tile_seven():
    """The big fight with the big guy. Here user only survives if they have aquired the pistol,
    all other options = game over."""
    termcolor.cprint(images.bigfoot_img, 'red')
    bigfoot_options = ["1","2","3","4"]
    user_choice = ""
    print("You enter the big tree structure at the end of the meadow, not your best life choice,")
    print("you are now standing face to face with a huge bigfoot who plans to have you as a snack.")
    print("What will you do?\n")
    print("1. You know what, i will finish him with my bare FISTS!")
    print("2. Hell no, not today mr bigfoot! RUUUN!")
    print("3. Wait i can use my knife! AAATTAACCKKK!")
    print("4. HAH time to taste lead big guy. I shoot my pistol!! ")
    user_choice = str(input("Which option do you pick 1, 2, 3 or 4? \n"))
    while user_choice not in bigfoot_options:
        if user_choice == bigfoot_options[0]:
            print("Youre hallucinating, cant kill a bigfoot with your fists!")
            time.sleep(1)
            termcolor.cprint("Youre hallucinating, cant kill a bigfoot with your fists! You dead mr! Game over!", 'red')
            termcolor.cprint(images.dead_img, 'red')
            time.sleep(3)
            quit()
        elif user_choice == bigfoot_options[1]:
            print("Sayonara, cya later mr bigfoot")
            time.sleep(1)
            print("Outrun a bigfoot? worst idea ever")
            termcolor.cprint("Youre sleeping with the fishes now pal", 'red')
            termcolor.cprint(images.dead_img, 'red')
            time.sleep(3)
            quit()
        elif user_choice == bigfoot_options[2]:
            print("You are gonna taste my fury big guy, ive got a knife!!")
            time.sleep(1)
            termcolor.cprint("Bigfoot took your knife and used it as a toothpick while you being cooked over the flame", 'red')
            termcolor.cprint("Gave over dude, better luck next time...", 'red')
            termcolor.cprint(images.dead_img, 'red')
            quit()
        elif user_choice == bigfoot_options[3]:
            print("You fire your pistol at the bigfoot...")
            time.sleep(2)
            termcolor.cprint("The big guy makes a last loud growl while falling down to the ground, you did it!!!")
            termcolor.cprint("Wait, he dropped something, i need to investigate...", 'green')
            time.sleep(1)
            termcolor.cprint("Its a compass, should be useful! Now back to the meadow", 'yellow')
            loot.append("compass")
            meadow_tile_five()
    else:
        print("Please pick 1, 2, 3 or 4")

#def ocean_tile_eight():
#treehouse_tile_six()
#bigfoot_tile_seven()
main()
