# Imports
import images
# Contains ASCII images used in the application

# Username
username = ""


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
    print("What is your name?\n")
    while True:
        username = input("")
        if not username.isalpha():
            print(
                "Sorry, we don't know that language, please" +
                "use some letters we can understand"
            )
            continue
        else:
            print(f"Welcome {username}, let's begin")
            first_challenge()


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
        "A) Try to win a ship in a card game with sketchy " +
        "gamblers at the local drinking spot?"
        )
    print("B) Try to sneak onboard a ship leaving the shipyard as stowaways?")
    print("C) Get Grogu to steal someone's keys using the force")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print("You lose the game and now owe all the gamblers a drink!")
        end_game()
    elif user_choice == "B":
        print("You get found and chucked off the ship!")
        end_game()
    elif user_choice == "C":
        print("Grogu gets the keys and you find the ship, time to get going!")
        second_challenge()
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
    print("B) Try to fix it yourselves")
    print("C) Head back into town to try to get different ship")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print(
            "Peli Motto answers your call! She tells " +
            "you how to fix the ship and off you go"
            )
        third_challenge()
    elif user_choice == "B":
        print(
            "Grogu drops the spanner down a shoot" +
            "and you can't fix the ship"
            )
        end_game()
    elif user_choice == "C":
        print(
            "You head back to town and the gamblers " +
            "find you again and take grogu for yet another drink!"
        )
        end_game()
    else:
        print("You must choice A, B or C")


def third_challenge():
    """
    Outline the third options of the game and
    allows user to choose where the game will go
    """
    user_choice = ""
    print("Your ships just makes it to planet, although still falling apart")
    print("You head into the local Salon to find some more information")
    print(
        "Moth Giden troops have been spotted " +
        "on the other side of the planet"
    )
    print("Do you...")
    print("A) Get a speedster to get over there quick before they get away!")
    print("B) Get back on the ship and try to fly it across")
    print("C) Try to find our more info from the locals")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print("You've made it, but they are no where to be seen!")
    elif user_choice == "B":
        print(
            "AND CRASH. Sorry your ship is broken and it " +
            "will be a while before you can get it going again"
        )
        end_game()
    elif user_choice == "C":
        print("Grogu has been distracted by some eggs...")
        print(images.grogu)
        end_game()
    else:
        print("You must choice A, B or C")


def fourth_challenge():
    """
    Outline the fourth options of the game and
    allows user to choose where the game will go
    """
    user_choice = ""
    print("You get to other side of planet and they are not to be seen")
    print("But you find Mandos helmet")
    print("Do you...")
    print("A) Use the force to try to locate him")
    print("B) Cry and go home")
    print("C) Go and get the Mandalorian covenant to try to help")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print(
            "Grogu has found him! He is located " +
            "in a secret hideout a few clicks away!"
        )
        fifth_challenge()
    elif user_choice == "B":
        print("You go home and Mando is lost forever")
        end_game()
    elif user_choice == "C":
        print(
            "You get back to your ship to contact the " +
            "conenant but who knows when they'll get here!"
            )
        end_game()
    else:
        print("You must choice A, B or C")


def fifth_challenge():
    """
    Outline the fifth options of the game and
    allows user to choose where the game will go
    """
    user_choice = ""
    print("You have used the force and found he is still on the planet")
    print("Taking your speedster to go to where they are hiding")
    print("Do you...")
    print("A) Break in and resuce him")
    print("B) Wait until he is transported out to attack their ships then")
    print("C) Wait for help")
    user_choice = str(input("What do you deciede A,B or C? \n"))
    if user_choice == "A":
        print(
            "You've got him!! Well done for rescuing Mando!" +
            "You can now go and enjoy more adventures together!"
            )
        win_game()
    elif user_choice == "B":
        print(
            "You wait, and wait and they dont come back, you" +
            "deciede to go get help and miss their ship departing..."
            )
        end_game()
    elif user_choice == "C":
        print("Looks like no one is coming and Moth Giden got away!")
        end_game()
    else:
        print("You must choice A, B or C")


def end_game():
    """
    Ends the game and asks if the user wants to play again
    """
    print("Do you want to play again? y/n \n")
    user_input = str(input("").lower())
    if user_input == "y":
        print("Welcome back {username}, lets try again!!")
    elif user_input == "n":
        print(
            "Thanks for helping Grogu try to get Mando back!" +
            "Better luck next time!"
            )
        quit()
    else:
        print("You must choose yes or no")


def win_game():
    """
    Message to be displayed if they win the game
    """
    print("Do you want to play again? y/n \n")
    user_input = str(input("").lower())
    if user_input == "y":
        print("Welcome back {username}, lets go again!!")
        first_challenge()
    elif user_input == "n":
        print("Thanks for helping Grogu rescue his best pal!!")
        quit()
    else:
        print("You must choose yes or no")


def main():
    """
    Main functions in order
    """
    intro_text()


main()
