# Imports
import images
# Contains ASCII images used in the application


# Game Intro Text
def intro_text():
    """
    Introduction to the game, allows users to input their name
    and explains the story and journey they are about to go on
    """
    print(
        "Welcome to the game that will take you" +
        "on an out of space adventure!"
        )
    print("Can you help Grogu find his way back to Din Djarin?")
    print(images.logo_img)
    print(images.welcome_message)
    username = input("What is your name?\n")
    while True:
        username = input("")
        if not username.isalpha():
            print("Sorry, please use letters we can understand")
        else:
            print(f"Welcome {username}, let's begin")


def first_challenge():
    """
    Outlined the first options of the game
    and allows user to choose where the game will go
    """
    user_choice = ""
    print("You discover that Mando might be on Moth Gideons light cruiser")
    print("But you need a ship to be able to catch up to him")
    print("Do you...")
    print(
        "A) Try to win a ship in a card game with sketchy" +
        "gamblers at the local drinking spot?"
        )
    print("B) Try to sneak onboard a ship leaving the shipyard as stowaways?")
    print("C) Get Grogu to steal someone's keys using the force")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print("")
    elif user_choice == "B":
        print("")
    elif user_choice == "C":
        print("")
    else:
        print("You must choice A, B or C")


def second_challenge():
    """
    Outline the second options of the game and
    allows user to choose where the game will go
    """
    user_choice = ""
    print("You make it onto the ship")
    print("But the ship doesnt start")
    print("Do you...")
    print("A) Call the mechanic")
    print("B) Try to fix it yours")
    print("C) Get different ship")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print("")
    elif user_choice == "B":
        print("")
    elif user_choice == "C":
        print("")
    else:
        print("You must choice A, B or C")


def third_challenge():
    """
    Outline the second options of the game and
    allows user to choose where the game will go
    """
    user_choice = ""
    print("Get to planet and go to salon to find more infomation")
    print("Moth Giden trops have been spotted on the other side of the planet")
    print("Do you...")
    print("A) Get speedster")
    print("B) Get back on ship and try to fly")
    print("C) Get distracted by eggs")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print("")
    elif user_choice == "B":
        print("")
    elif user_choice == "C":
        print("")
    else:
        print("You must choice A, B or C")


def fourth_challenge():
    """
    Outline the second options of the game and
    allows user to choose where the game will go
    """
    user_choice = ""
    print("Get to planet and go to salon to find more infomation")
    print("Moth Giden trops have been spotted on the other side of the planet")
    print("Do you...")
    print("A) Get speedster")
    print("B) Get back on ship and try to fly")
    print("C) Get distracted by eggs")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print("")
    elif user_choice == "B":
        print("")
    elif user_choice == "C":
        print("")
    else:
        print("You must choice A, B or C")


def fifth_challenge():
    """
    Outline the second options of the game and
    allows user to choose where the game will go
    """
    user_choice = ""
    print("Get to other side of planet and they are not to be seen")
    print("But you find Mandos helmet")
    print("Do you...")
    print("A) Use the force to try to locate him")
    print("B) Cry and go home")
    print("C) Go and get the covenant to help")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print("")
    elif user_choice == "B":
        print("")
    elif user_choice == "C":
        print("")
    else:
        print("You must choice A, B or C")


def sixth_challenge():
    """
    Outline the second options of the game and
    allows user to choose where the game will go
    """
    user_choice = ""
    print("You have used the force and found he is still on the planet")
    print("Taking your speedster to go to where they are hiding")
    print("Do you...")
    print("A) Break in and resuce him")
    print("B) Wait until he is transported out to attack then")
    print("C) Wait for help from the covenant")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print("")
    elif user_choice == "B":
        print("")
    elif user_choice == "C":
        print("")
    else:
        print("You must choice A, B or C")


def main():
    """
    Main functions in order
    """
    intro_text()
    first_challenge()
    second_challenge()
    third_challenge()


main()
