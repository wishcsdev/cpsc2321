# Vishaal Bakshi
# Assignment 3: Decomposing a problem into functions.
# CPSC231
state_pantry = 4        # Invalid state of the pantry.      
state_kitchen = 3       # Invalid state of the kitchen.
is_stage2 = 0           # Flag to set that we are in stage 2.

def enterance_room():
    enterance_input = 4         # Invalid state of enterance_input from user
    global is_stage2
    
    while (enterance_input > 3 or enterance_input == 0):
        print("Welcome to the enterance room.\n")
        print("1. Unlock Door.")
        print("2. Take Right Walkway.")
        print("3. Take Left Walkway.\n\n")
        enterance_input = input();
        print("You chose option " + str(enterance_input))

        # User selected to unlock the door.
        if enterance_input == 1:
            # Check if door is unlocked.
            if (check_stage1_state()):
                is_stage2 = 1
                return
            else:                                        # Door is not locked. Try again.
                 print("Door Locked. Try again\n\n")
                 enterance_input = 4                     # Trick to stay in inside loop

    # Check if user selected to enter the pantry.
    if (enterance_input == 2):
        pantry_room()

    # Check if user selected to enter the kitchen.
    if (enterance_input == 3):
        kitchen_room()
        
    return 0

def pantry_room():
    temp_input = 5
    global state_pantry
    while (temp_input > 4 or temp_input == 0):
        print ("Welcome to Pantry Room. Set up the dial. \n 1. Blue \n 2. Red \n 3. Green \n 4. Exit without change\n\n")
        temp_input = input()
        state_pantry = temp_input
        print(state_pantry)

        
def kitchen_room():
        temp_input = 4
        global state_kitchen
        while (temp_input > 3 or temp_input == 0):
            print ("Welcome to Kitchen Room. Set up the lever. \n 1. Front \n 2. Back \n 3. Exit without change \n\n")
            temp_input = input()
            state_kitchen = temp_input
            print(state_kitchen)
            
def check_stage1_state():
    if (state_kitchen == 2) and (state_pantry == 2):
        return 1
    else:
        return 0

is_livingroom_potofsoil_fertilized = 0
is_ballofstring_picked = 0
is_ballofstring_dropped = 0
is_user_got_some_cheese = 0

def living_room(_is_ballofstring_picked, _is_livingroom_potofsoil_fertilized):
    user_input = 5
    global is_ballofstring_picked

    while (user_input > 4 or user_input == 0):
        print("Welcome to the living room. \n")
        print("Choose from the following options:\n")
        print("1. View the pot of soil.")
        print("2. Take the Stairs to the attic.")
        print("3. Take the Dark enteranceway to the bedroom.")
        if (_is_ballofstring_picked == 0):
            print("4. Pick up ball of string.\n")
        user_input = input()

        if (user_input == 1):
            if (_is_livingroom_potofsoil_fertilized):
                print("WELCOME TO PARADISE. YOU WIN!")
                return 1
            else:
                print("Vine is DRY.\n")
        elif (user_input == 2):
            attic_room(_is_ballofstring_picked)
            return 0
        elif (user_input == 3):
            bedroom_room(is_ballofstring_picked, is_ballofstring_dropped, is_user_got_some_cheese)
            return 0
        elif (user_input == 4 and is_ballofstring_picked == 0):
            is_ballofstring_picked = 1
            _is_ballofstring_picked = is_ballofstring_picked
        user_input = 5
        
    return 0

def attic_room(_is_ballofstring_picked):
    user_input = 5

    while (user_input > 4 or user_input == 0):
        print("Welcome to the Attic.\n")
        print("1. Pick up some cheese and drop it.")
        print("2. Pick up some cheese and carry it with you.")
        print("3. Return to the livingroom via the stairs.")
        if (_is_ballofstring_picked and is_ballofstring_dropped == 0):
            print("4. Drop the string down the hole to distract TomCat.\n")

        user_input = input()    
        if (user_input == 1):
            print("Cheese is too big.\n")
        elif (user_input == 2):
            global is_user_got_some_cheese
            is_user_got_some_cheese = 1
        elif (user_input == 3):
            # Return to living room
            return                    # return so as to not call living_room() recursively.
        elif (user_input == 4 and is_ballofstring_dropped == 0):
            # Drop string
            global is_ballofstring_dropped
            is_ballofstring_dropped = 1

        user_input = 5
    return

def bedroom_room(_is_ballofstring_picked, _is_ballofstring_dropped, _is_user_got_some_cheese):
    user_input = 10

    while (user_input > 3 or user_input == 0):
        print("Welcome to bedroom.\n")
        if (_is_ballofstring_dropped):
            print("1. Mouse wants to be fed. Feed it!")
        elif (_is_ballofstring_picked):
            print("2. Play with Cat.")
        print ("3. Return to livingroom.\n")

        user_input = input()
        if (user_input == 1):
            print("Mouse was fed and is back for more if you would like :).\n")
            global is_livingroom_potofsoil_fertilized
            is_livingroom_potofsoil_fertilized = 1
            user_input = 10
        elif (user_input == 2):
            print("Cat had fun playing but is back to hunting the mouse :(.\n")
            user_input = 10
        elif (user_input == 3):
            print("Returning to livingroom.\n")
            return
    return

# Entry point to the game. This is the first function that is run and contains
# the superloop for the game. 
def main():
    print("Welcome to the game.\n")
    
    # Superloop of the game.
    while 1:
        # Check if user is in stage2    
        if (is_stage2):
            # Returns true if stage1 is complete.
            print("Entering stage2.\n")
            if (living_room(is_ballofstring_picked, is_livingroom_potofsoil_fertilized)):
                return              # Game over.
        else:
            enterance_room()
            # User still in stage 1.
            if (state_pantry == 1):
               print("Dial set to Blue")
            elif (state_pantry == 2):
               print("Dial set to Red")
            elif (state_pantry == 3):
               print("Dial set to Green")
            elif (state_pantry == 4):
               print("Dial Not set")

            if (state_kitchen == 1):
                print("Kitchen lever pushed Forward\n\n")
            elif (state_kitchen == 2):
                print("Kitchen lever pushed Backward\n\n")
            elif (state_kitchen == 3):
                print("Kitchen lever not set.\n\n")        
    return

main()

