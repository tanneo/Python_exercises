#Branches and functions
from sys import exit #import exit module. This module used to exit program

def gold_room(): 
    print("This room is full of gold. How much do you take?") #check how much gold user wants

    choice = input('Enter a number:') #user input
    if "0" in choice or "1" in choice:
        how_much = int(choice) #if zero of 1 in choice, change users choice to integer and assign to variable called how_much
    else:
        dead("Man, learn to type a number") #if no 0 or 1 in choice, call dead function, which will print to user and exit program

    if how_much < 50: #if user input less than 50, let the user know they won and exit program
        print("Nice, you are not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!") #if user input =>50, call dead function to exit program

def bear_room():
    print('There is a bear here')
    print('The bear has a bunch of honey')
    print('The fat bear is in front of another door')
    print('How are you going to move the bear?') #ask for user input
    bear_moved = False #set bear moved varilable to False boolean

    while True: #create while loop for while the bear hasn't moved is set to true
        choice = input('>')

        if choice == "take honey": #if choice is take honey, call dead function
            dead("The bear looks at you and slaps your face off")
        elif choice == "taunt bear" and not bear_moved: #if bear hasn't moved and choice is to taunt bear, set bear moved to True 
            print("The bear has moved from the door")
            print("You can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved: #if user chooses to taunt bear again when it has been moved, kill player
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved: #once bear has been moved, if user chooses to open door, they will go to gold room
            gold_room()
        else:
            print("I got no idea what that means!") #if user enters anything else, let them know program doesn't understand their input

def cthulu_room():
    print("Here you see the great evil Cthulu")
    print("He, it, whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head?")

    choice = input('>')

    if "flee" in choice:
        start() #if input flee, take back to start function where the program will begin
    elif "head" in choice:
        dead('Well that was tasty') #dead
    else:
        cthulu_room() #keep redirecting to ask user if they want to flee for life or eat head

def dead(why):
    print(why, "Good job!")
    exit(0) #exits program

def start():
    print("You are in a dark room")
    print("There is a door to your right and left!")
    print("Which one do you take?")

    choice = input(">")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve")

start()