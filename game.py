print("You walk into a forest. Which way do you turn?")
print("Press 1. to turn left")
print("Press 2. to turn right")

unicorn = input(">")

if unicorn == "1":
    print("Good job! You climb onto the unicorns back!")
    print("Press 1. to fly over the mountains")
    print("Press 2. to fly over the ocean")
    flight = input(">")
    if flight == "1":
        print("You have run into an issue! There is a crazy Giant ahead!")
        print("What do you do?")
        print("Press 1. to go into battle with the giant")
        print("Press 2. to go around the giant")
        print("Press 3. to offer the giant a beer and hope he lets you past!")
        giant = input(">")
        if giant == "1":
            print("The giant blows his nose on your face and you drown in his SNOT! Well done! You die")
        elif giant == "2":
            print("You went around the giant but took a wrong turn")
            print("It is now night time and the vampires come out soon")
            print("What do you do?")
            print("Press 1 to continue")
            print("Press 2 to hide with the unicorn in a nearby cabin until morning")
            night = input(">")
            if night == "1":
                print("The vampire is actually nice and takes you back to their coven for a hot shower! You have made it another night!")
            elif night == "2":
                print("On the way back to the coven the unicorn gets attacked by an overgrown toad. You both die instantly!")
            else:
                print("You are a miserable wimp")
        else:
            print("f{giant} is probably a better idea anyway. Rocky the dog saw you and took you to his puppy home to safety")

    elif flight == "2":
        print("Congrats! You have come across a dragon that is willing to help you!")
        print("What do you do?")
        print("Press 1. Jump off the unicorn and onto the dragon")
        print("Press 2. to stay on the unicorn and try your luck")
        dragon = input(">")
        if dragon == "1":
           print("The dragon tricked you and incinerates you with his flames! Congrats. You died!") 
        elif dragon =="2":
           print("The unicorn strikes the dragon with his hoof and gets you to safety! You have reached level 2!") 
        else:
            print("You fell off the unicorn and drowned in the ocean! Start again!")
    else:
        print("Good job! Billie the Chihuahua has taken you to safety!")

elif unicorn == "2":
    print("The unicorn couldn't get to you in time! The dragon bites your head off!")
else:
    print(f("Maybe {unicorn} is the best option! The unicorn returns you back to safety"))