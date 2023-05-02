# Bigfoot Rage

### A fun game about survival in the forest, finding loot, and avoiding being killed by... you guessed it bigfoot!   
### Will you make it out alive?    
      

### Link to the finished game: [PLAY](https://bigfoot-rage.herokuapp.com/)
_____________________________________________________________________________
## Content:
- [Am i responsive image](#am-i-responsive-image)
- [Lucid Chart](#lucid-chart)
- [Project Goals and Audience](#project-goals-and-target-audience)
- ### Design and UX
    - [Design and Features](#design-and-features)
    - [Colour Scheme](#colour-scheme)
    - [User Experience](#user-experience-ux)
        - [User Stories](#user-stories)
        - [Game graphics](#game-graphics)
    - [Typography](#typography)
    - [Imagery](#imagery)
- ### Technologies Used
    - [Languages used](#languages)
    - [Frameworks, Packages & Programs Used](#frameworks-packages--programs-used)
- ### Testing
    - [PEP8](#pep8)
    - [Lighthouse](#lighthouse)
    - [Bug testing](#bug-testing)
    - [Responsiveness](#responsiveness-and-further-testing)
    - [Fixed bugs](#fixed-bugs)
- ### Deployment
    - [Deployt to Heroku](#deployment)
- ### Credits
    - [Code](#code)
    - [Content](#contents)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)



_____________________________________________________________________________
## Am i responsive image 
![Screenshot](/assets/images/amiresponsive.png)
_____________________________________________________________________________
## Lucid chart
![Screenshot](/assets/images/bigfoot_rage_lucid.png)  
_____________________________________________________________________________ 
## Project goals and target audience.  
### Achieved:
- Build a fun game with Python that lets you choose different options and outcomes.
- Make a website that also has the same theme as the game.
- Being able to add new options and more content easily in the future.
- Be easy to understand and navigate

### Future projects: 
- Add more items to the game and available content.
- Would love to add some fighting mechanics.
- More options to create a unique avatar with stats, hp, strength, etc.    

## Audience:
- This game is for everyone, older people for the nostalgic feel of play and art,
The younger generation can see and learn how games were back then.   
[Back to top](#bigfoot-rage)
_____________________________________________________________________________ 
## Design and features:   
- The whole design is based on the 80s/90s video game vibe. The colourful terminal and the bigfoot background image add a nice touch.    
![Screenshot](/assets/images/website-landing-page.png)       
- Feature 1 is the button that starts the game. Easily visible.      
![Screenshot](/assets/images/bigfoot_runprogram.png)       
- Feature 2 is a footer with links to the creator's LinkedIn and GitHub repository.     
![Screenshot](/assets/images/bigfoot-footer.png)  
_____________________________________________________________________________  
## Colour Scheme
- Imported termcolor to change the colors in the terminal.
Available colors in termcolor below:    
![Screenshot](/assets/images/termcolor_palette.png)   
- Colors from background, that is also used on button and footer    
![Screenshot](/assets/images/color-palette.png)  
_____________________________________________________________________________  
## User Experience (UX)

### User Stories
- Play a fun text-based game.
- Interact with the game through available choices.
- Have different outcomes based on choices.
- Get feedback when making choices.
- Included easter egg that shows a surprise tile if you find all map pieces.      

### Game graphics
- Display_intro - greets the user when they start the game, gives a welcome message and information on how to play the game, and lets the user type in its name.   
- start_game_tile_one - This is the first tile of the game, with an intro text that explains your situation and asks you what option you want to pick to continue to play the game.
![Screenshot](/assets/images/game-tiles-1.png)  
_____________________________________________________________________________     
- crossroad_tile_two - Here, the user is shown the first of many ascii arts in the game; this shows a spooky tree. When you enter the crossroads, the user will have four options: explore more or even go back to the tent.   
- cabin_tile_three - Shows the user a cabin in yellow; there are only two options.   
![Screenshot](/assets/images/game-tiles-2.png)   
_____________________________________________________________________________  
- wolf_den_tile_four - Here, the user will encounter the wolf; options are to run away with a success rate of 66%, can fight with your Fists or use your knife if you happen to find it.
- meadows_tile_five - Another crossroad tile leaves the user with four options and ASCII art of a magenta flower.       
![Screenshot](/assets/images/game-tiles-3.png)   
_____________________________________________________________________________ 
- treehouse_tile_six - Welcomes you with a green ASCII image of a treehouse, with three options, you can explore, stay the night, or go back.   
- bigfoot_tile_seven - Big fight in the game; it's now or never. There's only one option that will keep you alive!         
![Screenshot](/assets/images/game-tiles-4.png)   
_____________________________________________________________________________ 
- ocean_tile_eight - A beautiful blue palm invites you to the ocean, three options, and it can be the last tile if the user has done Everything right!
- escape_tile_nine - Shows when you have finished the game. Big green text "You escaped" and congratulations.         
![Screenshot](/assets/images/game-tiles-5.png)     
_____________________________________________________________________________  

## Typography
- Standard terminal output with termcolor to colour the text.
_____________________________________________________________________________
## Imagery
- I wanted the game to be more than text, so I used some ASCII art from fsymbols, which makes the game more alive and eye-catching.  
- Used midjourney AI to make the background image.
![Screenshot](/assets/images/bigfoot-wallpaper1.png)   
[Back to top](#bigfoot-rage)
_____________________________________________________________________________  
## Languages
![Screenshot](/assets/images/languages_used.png)
- HTML5 from CodeInstitute Template(some own modifications to style the website)
- CSS from CodeInstitute Template(some own modifications to style the website)
- Javascript from CodeInstitute Template
- Python code, all done by myself
____________________________________________________________________________  
## Frameworks, Packages & Programs Used
- Lucidchart for overwiev of code.
- Google Sheets to make a bug testing sheet.
- Packages used:
    - random
    - time
    - sys
    - termcolor cprint   
[Back to top](#bigfoot-rage)
____________________________________________________________________________  
## Testing

### PEP8
- Pylinter used in gitpod and shows no problems with code.    
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)   

### Lighthouse
- ### Desktop
![Screenshot](/assets/images/lighthouse_desktop.png)
- ### Mobile
![Screenshot](/assets/images/lighthouse_mobile.png)    

### Bug testing
Extensive testing was done by myself; a chart of that is available on this Google [SHEET](https://docs.google.com/spreadsheets/d/1N055Napmr7ulxI-0MoJhgC5cHyd6CvADoCtSoBDsyEQ/edit?usp=sharing)   
- This includes input checks.   
- Tile movement.   
- Game walkthrough with different loot orders.
- Making sure random() outcomes work.  

### Responsiveness and Further Testing
- The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge, and Safari browsers.
- Friends and family members were asked to review the site and documentation to identify bugs and user experience issues. 
- All content in the game has been looked at with Grammarly to check for sentence builds and spellchecking.
_____________________________________________________________________________  
## Fixed Bugs
- Had a problem with the outcome when you looted map and weapons in random order; fixed by changing how to check the lists and using len(), which works better.   

- Another issue was that if you wanted to play again, the loot lists didn't reset; you had to implement a clear() list function.   
[Back to top](#bigfoot-rage)
_____________________________________________________________________________  

## Deployment
Was deployed using Heroku with the following steps:

- Login to Heroku (Create an account if necessary)
- Click New in the Heroku dashboard and select ”Create new app.”
- Write a name for the app and choose your region and click ”Create App.”
- In the settings tab for the new application, created one Config name PORT and has a value of 8000
- Two build pack scripts were added: Python and Nodejs (in that order)
- Connect your Heroku with your GitHub account and the repository you are working on
- Then at the bottom, you can do a manual deployment or set it to automatic deployment to deploy every time your repo is updated.   
![Screenshot](/assets/images/heroku_deployment.png)   
[Back to top](#bigfoot-rage)

_____________________________________________________________________________  

## Credits.  

### Code.  

- How to set an input to a string [stackoverflow](https://stackoverflow.com/questions/53173087/input-in-python-to-be-only-in-string)  

- Page to learn how to use termcolor [Link](https://replit.com/talk/learn/How-to-Use-Termcolor-In-Python/24684)  

- How to create two files in Python and import variables [stackoverflow](https://stackoverflow.com/questions/17255737/importing-variables-from-another-file)   

- How to import time and use it on [realpython](https://realpython.com/python-sleep/#:~:text=Adding%20a%20Python%20sleep()%20Call%20With%20time.sleep(),-Python%20has%20built&text=The%20time%20module%20has%20a,however%20many%20seconds%20you%20specify.&text=If%20you%20run%20this%20code,new%20statement%20in%20the%20REPL)

- How to get two print functions on the same line [Link](https://www.pylenin.com/blogs/python-print/#:~:text=To%20print%20multiple%20expressions%20to,same%20line%20in%20Python%203.&text=With%20Python%203%2C%20you%20do,print%20on%20the%20same%20line)   

- Post about sys and how to use it to remove printed text [stackoverflow](https://stackoverflow.com/questions/53173087/input-in-python-to-be-only-in-string)

- Learned how to clear a list when you restart the game [techiedelight](https://www.techiedelight.com/remove-all-items-from-list-python/)

- A video by Doug Mcnally on how to make a text-based game used his idea to check for input validation. [video link](https://www.youtube.com/watch?v=miuHrP2O7Jw&ab_channel=DougMcNally)

- Got help styling the website by looking at Alexa's project; play it; a lot of fun! [Harry Potter Adventure Game](https://github.com/AlexaH88/harry-potter-adventure-game)


### Contents  
- The developer wrote all content.

### Media  
- All ASCII art came from [fsymbols](https://stackoverflow.com/questions/53173087/input-in-python-to-be-only-in-string)
- Background image made in midjourney [Link](https://www.midjourney.com/app/)

### Acknowledgements
- My Mentor for continuous helpful feedback.

- Tutor support at Code Institute for their support.    
[Back to top](#bigfoot-rage)

_____________________________________________________________________________   
