import images #contains ASCII images used in the application 

def intro_text():
    """Introduction to the game, allows users to input their name, 
    and explains the story and journey they are about to go on
    """
    print(images.logo_img)
    print("Welcome to the command-line game that will take you on an out of space adventure!")
    print("Can you help Grogu find his way back to Din Djarin?")

intro_text()
print(images.welcome_message)
username = input("What is your name? ")
print(username)