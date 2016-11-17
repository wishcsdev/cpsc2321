# So read my comments. Its very pseudo-code. It will be best to read this and rewrite it as you want. There are going to be bugs for sure so just remember to think it out
# through and fix them.

# This is where you enter the game. You enter at the Enterance.
print("Game Begin/n");

exit_entrance_loop = 0
pantry_state = 4
kitchen_state = 3

while exit_entrance_loop == 0:
    # This is the main loop of the program where the game is running.
    # This is similar to most games which actually have a loop like this where they dispatch multiple threads to handle UI, logic and other gaming intetactions.
    # Our game only has one simple sequential loop which will take care of business.0

    if (pantry_state == 1):
       print("Dial set to Blue")
    elif (pantry_state == 2):
       print("Dial set to Red")
    elif (pantry_state == 3):
       print("Dial set to Green")
    elif (pantry_state == 4):
        print("Dial Not set")

    if (kitchen_state == 1):
       print("Kitchen lever pushed Forward\n\n")
    elif (kitchen_state == 2):
       print("Kitchen lever pushed Backward\n\n")
    elif (kitchen_state == 3):
       print("Kitchen lever not set.\n\n")

    # ENTERANCE LOOP.
    print("Choose your options wisely.")
    print("1. Unlock Door.")
    print("2. Take Right Walkway.")
    print("3. Take Left Walkway.\n\n")
    enterance_input = 4                      # Use this variable to keep asking the player for the proper input.
    while (enterance_input > 3 or enterance_input == 0):
        enterance_input = input();
        print("You chose option " + str(enterance_input))
        if enterance_input > 3 or enterance_input == 0:
            print("Invalid Option. Try again")
            print("Choose your options wisely.")
            print("1. Unlock Door.")
            print("2. Take Right Walkway.")
            print("3. Take Left Walkway.\n\n")


        if enterance_input == 1:
            if (pantry_state == 2) and (kitchen_state == 2):
                print("You won! Go get a life now.\n\n")
                exit_entrance_loop = 1
                enterance_input = 2                      # Just a little trick to exit this inside loop.
            else:
                 print("Door Locked. Pick another option\n\n")
                 enterance_input = 4                     # Trick to stay in inside loop


    # PANTRY BRANCH
    if (enterance_input == 2):
        print ("Welcome to Pantry Room. Set up the dial. \n 1. Blue \n 2. Red \n 3. Green \n 4. Exit without change\n\n")
        temp_input = input()
        while (temp_input > 4 or temp_input == 0):
            print("Invalid Entry. Try again.")
            temp_input = input()

        pantry_state = temp_input

    # KITCHEN BRANCH
    if (enterance_input == 3):
        print ("Welcome to Kitchen Room. Set up the lever. \n 1. Front \n 2. Back \n 3. Exit without change \n\n")
        temp_input = input()
        while (temp_input > 3):
            print("Invalid Entry. Try again.")
            temp_input = input()

        if temp_input != 3:
            kitchen_state = temp_input