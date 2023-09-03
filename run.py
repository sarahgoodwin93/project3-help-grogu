# Imports 
import images 
# Contains ASCII images used in the application 


# Game Intro Text
def intro_text():
    """
    Introduction to the game, allows users to input their name 
    and explains the story and journey they are about to go on
    """
    print("Welcome to the game that will take you on an out of space adventure!")
    print("Can you help Grogu find his way back to Din Djarin?")
    print(images.logo_img)


intro_text()
print(images.welcome_message)
username = input("What is your name?\n")
print(f"Welcome {username}, let's begin")

first_challenge()
print("You discover that Mando might be on Moth Gideons light cruiser")
print("BUt you need a ship to be able to catch up to him")
print("Do you...")
print("A) Try to win a ship in a card game with sketchy gamblers at the local drinking spot?")
print("B) Try to sneak onboard a ship leaving the shipyard as stowaways?")
print("C) Get Grogu to steal someone's keys using the force")
user_choice = str(input("What do you deciede A,B or C? \n"))
if user_choice == 