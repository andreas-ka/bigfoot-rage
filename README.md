# Bigfoot Rage

### A fun game about survival in the forest, finding loot and avoid being killed by... you guessed it bigfoot!.   
### Will you make it out alive?       
_____________________________________________________________________________
### Am i responsive
![Screenshot](/assets/images/amiresponsive.png)
_____________________________________________________________________________
### Lucid chart
![Screenshot](/assets/images/bigfoot_rage_lucid.png)  
_____________________________________________________________________________ 

## User Experience (UX)


### User stories    
_____________________________________________________________________________  

#### First Time Visitor Goals   

As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the organisation.
As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
As a First Time Visitor, I want to look for testimonials to understand what their users think of them and see if they are trusted. I also want to locate their social media links to see their followings on social media to determine how trusted and known they are.   

#### Returning Visitor Goals     

As a Returning Visitor, I want to find information about coding challenges.
As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.
As a Returning Visitor, I want to find community links.   

#### Frequent User Goals   

As a Frequent User, I want to check to see if there are any newly added challenges or hackathons.
As a Frequent User, I want to check to see if there are any new blog posts.
As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.  

_____________________________________________________________________________  

### Design   

_____________________________________________________________________________  

#### Colour Scheme
- Imported termcolor to change the colors in the terminal.
Available colors in termcolor below:    
![Screenshot](/assets/images/termcolor_palette.png)   
- Colors from background, that is also used on button and footer    
![Screenshot](/assets/images/color_palette_background.png) 

_____________________________________________________________________________  

#### Typography
Standard terminal output

_____________________________________________________________________________  

#### Imagery
I really wanted the game to be more then text so i used some ascii art from fsymbols,   
makes the game more alive and eye catching.

_____________________________________________________________________________  
 

### Languages Used  
   
![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/120px-HTML5_logo_and_wordmark.svg.png)
![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/120px-CSS3_logo_and_wordmark.svg.png)
![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/121px-Python-logo-notext.svg.png)
  
____________________________________________________________________________  

### Frameworks, Libraries & Programs Used

- Lucidchart for overwiev of code.

- Google Sheet to make a bug testing sheet.

## Testing

- Pylinter used in gitpod and shows no problems with code.    
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

_____________________________________________________________________________  

### Bug testing
Extensive testing done by myself, chart of that is available on this google [SHEET](https://docs.google.com/spreadsheets/d/1N055Napmr7ulxI-0MoJhgC5cHyd6CvADoCtSoBDsyEQ/edit?usp=sharing)   
- This includes input checks.   
- Tile movement.   
- Game walktrough with different loot order.
- 
_____________________________________________________________________________  

## Further Testing
- The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues. 
- All content in the game has been looked at with Grammarly to check for sentence builds and spellchecking.

_____________________________________________________________________________  

## Fixed Bugs
- Had problem with the outcome when you looted map and weapons in a random order, fixed with changing how to check the lists, used len() and that works better.   

- Other issue was that if you wanted to play again the loot lists didnt reset, had to implement a clear() list function.
  
_____________________________________________________________________________  

## Deployment
GitHub Pages
The project was deployed to GitHub Pages using the following steps...   

_____________________________________________________________________________  

## Credits.  

### Code.  

- How to set an input to a string [stackoverflow](https://stackoverflow.com/questions/53173087/input-in-python-to-be-only-in-string)  

- Page to learn how to use termcolor [Link](https://replit.com/talk/learn/How-to-Use-Termcolor-In-Python/24684)  

- How to create two files in python and import variables [stackoverflow](https://stackoverflow.com/questions/17255737/importing-variables-from-another-file)   

- How to import time and use it on [realpython](https://realpython.com/python-sleep/#:~:text=Adding%20a%20Python%20sleep()%20Call%20With%20time.sleep(),-Python%20has%20built&text=The%20time%20module%20has%20a,however%20many%20seconds%20you%20specify.&text=If%20you%20run%20this%20code,new%20statement%20in%20the%20REPL)

- How to get two print functions on the same line [Link](https://www.pylenin.com/blogs/python-print/#:~:text=To%20print%20multiple%20expressions%20to,same%20line%20in%20Python%203.&text=With%20Python%203%2C%20you%20do,print%20on%20the%20same%20line)   

- Post about sys and how to use it to remove printed text [stackoverflow](https://stackoverflow.com/questions/53173087/input-in-python-to-be-only-in-string)

- Learned how to clear a list when you restart the game [techiedelight](https://www.techiedelight.com/remove-all-items-from-list-python/)

- A video by Doug Mcnally how to make a text based game, used his idea to check for input validation. [video link](https://www.youtube.com/watch?v=miuHrP2O7Jw&ab_channel=DougMcNally)

- Got help styling the website by looking at Alexa's project, go play it, alot of fun! [Harry Potter Adventure Game](https://github.com/AlexaH88/harry-potter-adventure-game)


### Content.  
- All content was written by the developer.

### Media.  
- All ascii art came from [fsymbols](https://stackoverflow.com/questions/53173087/input-in-python-to-be-only-in-string)

### Acknowledgements
- My Mentor for continuous helpful feedback.

- Tutor support at Code Institute for their support.

_____________________________________________________________________________   
