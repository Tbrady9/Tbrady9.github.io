
# Storing a variable for each item in the game and setting the value to 1 to show the item has not been picked up
# A 1 will indicate the item has not been picked up (0 means picked up)
grapple_gun = 1
batsuit = 1
kryptonite = 1
belt = 1
cure = 1
batarangs = 1
smoke_pellets = 1
gadget_count = 0


# Storing a game_over variable (0 = game still in session, 1 = loss, 2 = win)
game_over = 0


# Storing values for each room to signify where the player is (1 = player currently in the room)
mnrm = 0
crmlb = 0
cstmvlt = 0
eqmtrm = 0
trngrm = 0
mdby = 0
tclb = 0
krptvlt = 0
hngr = 0

# Storing the crime lab function to be called each time a person enters the crime lab
def crime_lab():
    # Calling global variables to be updated within this function
    global direction
    global grapple_gun
    global crmlb
    global mnrm
    global krptvlt
    global gadget_count
    crmlb -= 1
    # if the item hasn’t been picked up, prompt the user to pick it up, else prompt for direction of travel
    if grapple_gun == 1:
        print('You have entered the crime lab')
        print('Item Available: Grapple Gun')
        take_grapple_gun = input('Would you like to take the grapple gun? [Y/N]')
        while str.upper(take_grapple_gun) not in ['Y', 'N']:
            print('Please enter Y or N')
            take_grapple_gun = input('Would you like to take the grapple gun? [Y/N]')
        if str.upper(take_grapple_gun) == 'Y':
            grapple_gun -= 1
            gadget_count += 1
            print('You took the grapple gun and added it to your utility belt')
        elif str.upper(take_grapple_gun) == 'N':
            print('You leave the grapple gun where it is and continue your journey')
    else:
        print('You have entered the crime lab')
    direction = input('What direction would you like to travel? [South, East]')
    while str.upper(direction) not in ['SOUTH', 'EAST']:
        if str.upper(direction) in ['NORTH', 'WEST']:
            print('There are no rooms in that direction')
            direction = input('What direction would you like to travel? [South, East]')
        else:
            direction = input('Please enter South or East')
    else:
        if str.upper(direction) == 'SOUTH':
            krptvlt += 1
            print('You travel south')
        elif str.upper(direction) == 'EAST':
            mnrm += 1
            print('You travel east')


# Storing a costume vault function to be called every time a person enters the costume vault
def costume_vault():
    # Calling global variables to be updated in this function
    global batsuit
    global direction
    global cstmvlt
    global mnrm
    global eqmtrm
    global gadget_count
    cstmvlt -= 1
    print (cstmvlt)
    # This is part of the tutorial and forces the player to take the item and move to the east on the first visit.
    # The user will have free roam after that
    if batsuit > 0:
        print('You have entered the costume vault')
        print('Item Available: Batsuit')
        take_batsuit = input('Would you like to put on the batsuit? [Y/N]')
        while str.upper(take_batsuit) not in ['Y', 'N']:
            print('Please enter Y or N')
            take_batsuit = input('Would you like to put on the batsuit? [Y/N]')
        if str.upper(take_batsuit) == 'Y':
            batsuit -= 1
            gadget_count += 1
            print('You put on the batsuit and become one with the night')
        elif str.upper(take_batsuit) == 'N':
            print('You leave the Batsuit where it is. Maybe super rich Bruce Wayne can just pay off super mad Superman.')
            suit_count = 0
            while str.upper(take_batsuit) == 'N':
                if suit_count == 0:
                    take_batsuit = input('Seriously, you should probably put on the suit [Y/N]')
                    suit_count += 1
                elif suit_count == 1:
                    print('Come on!  It''s not the George Clooney suit with the nipples, I promise!')
                    take_batsuit = input('Put on the suit [Y/N]')
                    suit_count += 1
                elif suit_count > 1:
                    take_batsuit = input('Just put on the suit! [Y/N]')
            else:
                batsuit -= 1
                gadget_count += 1
                print('I knew you would come around.  Welcome to the game, Dark Knight!')
    else:
        print('You have entered the costume vault')
    if batsuit == 0 and belt == 0:
        direction = input('What direction would you like to travel? [South, East]')
        while str.upper(direction) not in ['SOUTH', 'EAST']:
            if str.upper(direction) in ['NORTH', 'WEST']:
                print('There are no rooms in that direction')
                direction = input('What direction would you like to travel? [South, East]')
            else:
                direction = input('Please enter South or East')
        else:
            if str.upper(direction) == 'SOUTH':
                mnrm += 1
                print('You travel south')
            elif str.upper(direction) == 'EAST':
                eqmtrm += 1
                print('You travel east')


# Storing a equipment room function to be called every time a person enters the equipment room
def equipment_room():
    # Calling global variables to be updated in this function
    global belt
    global direction
    global cstmvlt
    global eqmtrm
    global gadget_count
    eqmtrm -= 1
    # if the item hasn’t been picked up, prompt the user to pick it up, else prompt for direction of travel
    if belt > 0:
        print('You have entered the equipment room')
        print('Item Available: Utility Belt')
        take_belt = input('Would you like to put on the utility belt? [Y/N]')
        while str.upper(take_belt) not in ['Y', 'N']:
            print('Please enter Y or N')
            take_belt = input('Would you like to put on the utility belt? [Y/N]')
        if str.upper(take_belt) == 'Y':
            belt -= 1
            gadget_count += 1
            print('You put on the utility belt.  The batsuit is now complete.')
        elif str.upper(take_belt) == 'N':
            while str.upper(take_belt) == 'N':
                take_belt = input('You''re going to need that belt! [Y/N]')
            else:
                belt -= 1
                gadget_count += 1
    else:
        print('You have entered the equipment room')
    direction = input('What direction would you like to travel? [West]')
    while str.upper(direction) != 'WEST':
        if str.upper(direction) in ['NORTH', 'SOUTH', 'EAST']:
            print('There are no rooms in that direction')
            direction = input('What direction would you like to travel? [West]')
        else:
            print('West is the only way to go')
            direction = input('What direction would you like to travel? [West]')
    else:
        print('You travel west')
        cstmvlt += 1


# Storing the technology lab function to be called each time a person enters the technology lab
def technology_lab():
    # Calling global variables to be updated in this function
    global smoke_pellets
    global tclb
    global direction
    global mnrm
    global mdby
    global gadget_count
    tclb -= 1
    # if the item hasn’t been picked up, prompt the user to pick it up, else prompt for direction of travel
    if smoke_pellets == 1:
        print('You have entered the technology lab')
        print('Item Available: Smoke Pellets')
        take_smoke_pellets = input('Would you like to take the smoke pellets? [Y/N]')
        while str.upper(take_smoke_pellets) not in ['Y', 'N']:
            print('Please enter Y or N')
            take_smoke_pellets = input('Would you like to take the smoke pellets? [Y/N]')
        if str.upper(take_smoke_pellets) == 'Y':
            smoke_pellets -= 1
            gadget_count += 1
            print('You took the smoke pellets and added them to your utility belt')
        elif str.upper(take_smoke_pellets) == 'N':
            print('You leave the smoke pellets where they are and continue your journey')
    else:
        print('You have entered the technology lab')
    direction = input('What direction would you like to travel? [South or West]')
    while str.upper(direction) not in ['SOUTH', 'WEST']:
        if str.upper(direction) in ['NORTH', 'EAST']:
            print('There are no rooms in that direction')
            direction = input('What direction would you like to travel? [South or West]')
        else:
            print('West is the only way to go')
            direction = input('What direction would you like to travel? [South or West]')
    else:
        if str.upper(direction) == 'SOUTH':
            mdby += 1
            print('You travel south')
        elif str.upper(direction) == 'WEST':
            mnrm += 1
            print('You travel west')


# Storing the medical bay function to be called each time a person enters the medical bay
def medical_bay():
    # Calling global variables to be updated in this function
    global cure
    global mdby
    global tclb
    global trngrm
    global direction
    global gadget_count
    mdby -= 1
    # if the item hasn’t been picked up, prompt the user to pick it up, else prompt for direction of travel
    if cure == 1:
        print('You have entered the medical bay')
        print('Item Available: Cure')
        take_cure = input('Would you like to take the cure? [Y/N]')
        while str.upper(take_cure) not in ['Y', 'N']:
            print('Please enter Y or N')
            take_cure = input('Would you like to take the cure? [Y/N]')
        if str.upper(take_cure) == 'Y':
            cure -= 1
            gadget_count += 1
            print('You took the cure and added it to your utility belt')
        elif str.upper(take_cure) == 'N':
            print('You leave the cure where it is and continue your journey')
    else:
        print('You have entered the medical bay')
    direction = input('What direction would you like to travel? [North, West]')
    while str.upper(direction) not in ['NORTH', 'WEST']:
        if str.upper(direction) in ['SOUTH', 'EAST']:
            print('There are no rooms in that direction')
            direction = input('What direction would you like to travel? [North, West]')
        else:
            print('You can only travel North or West')
            direction = input('What direction would you like to travel?')
    else:
        if str.upper(direction) == 'NORTH':
            tclb += 1
            print('You travel north')
        elif str.upper(direction) == 'WEST':
            trngrm += 1
            print('You travel west')


# Storing the training room function to be called each time a person enters the training room
def training_room():
    # Calling global variables to be updated in this function
    global batarangs
    global direction
    global trngrm
    global hngr
    global mnrm
    global mdby
    global grapple_gun
    global kryptonite
    global smoke_pellets
    global cure
    global batarangs
    global gadget_count
    trngrm -= 1
    # if the item hasn’t been picked up, prompt the user to pick it up, else prompt for direction of travel
    if batarangs == 1:
        print('You have entered the training room')
        print('Item Available: Batarangs')
        take_batarangs = input('Would you like to take the batarangs? [Y/N]')
        while str.upper(take_batarangs) not in ['Y', 'N']:
            print('Please enter Y or N')
            take_batarangs = input('Would you like to take the batarangs? [Y/N]')
        if str.upper(take_batarangs) == 'Y':
            batarangs -= 1
            gadget_count += 1
            print('You took the batarangs and added them to your utility belt')
        elif str.upper(take_batarangs) == 'N':
            print('You leave the batarangs where they are and continue your journey')
    else:
        print('You have entered the training room')
    direction = input('What direction would you like to travel? [North, South, East]')
    while str.upper(direction) not in ['NORTH', 'SOUTH', 'EAST']:
        if str.upper(direction) == 'WEST':
            print('There are no rooms in that direction')
            direction = input('What direction would you like to travel? [North, South, East]')
        else:
            print('You can only travel North, South or East')
            direction = input('What direction would you like to travel?')
    else:
        if str.upper(direction) == 'NORTH':
            mnrm += 1
            print('You travel north')
        elif str.upper(direction) == 'EAST':
            mdby += 1
            print('You travel east')
        elif str.upper(direction) == 'SOUTH':
            print('You can hear the destruction being caused by Superman in the next room.')
            if grapple_gun == 1 or kryptonite == 1 or batarangs == 1 or cure == 1 or smoke_pellets == 1:
                print('You are unprepared for the battle that lies ahead.')
                go_on = input('Are you sure you want to continue South? [Y/N]')
                if str.upper(go_on) == 'Y':
                    hngr += 1
                    print('You travel south')
                elif str.upper(go_on) == 'N':
                    direction = input('What direction would you like to travel? [North, East]')
                    while str.upper(direction) not in ['NORTH', 'EAST']:
                        if str.upper(direction) == 'WEST':
                            print('There are no rooms in that direction')
                            direction = input('What direction would you like to travel? [North, East]')
                        elif str.upper(direction) == 'SOUTH':
                            print('You better get the rest of your equipment before facing Superman!')
                            direction = input('What direction would you like to travel? [North, East]')
                        else:
                            print('You can only go North or East')
                            direction = input('What direction would you like to travel? [North, East]')
                    else:
                        if str.upper(direction) == 'NORTH':
                            mnrm += 1
                            print('You travel north')
                        elif str.upper(direction) == 'EAST':
                            mdby += 1
                            print('You travel east')
                else:
                    go_on = input('Please enter Y or N')
            else:
                hngr += 1
                print('You travel south')


# Storing the technology lab function to be called each time a person enters the technology lab
def kryptonite_vault():
    # Calling global variables to be updated in this function
    global kryptonite
    global krptvlt
    global direction
    global crmlb
    global gadget_count
    krptvlt -= 1
    # if the item hasn’t been picked up, prompt the user to pick it up, else prompt for direction of travel
    if kryptonite == 1:
        print('You have entered the kryptonite containment vault')
        print('Item Available: Kryptonite Ring')
        take_kryptonite = input('Would you like to take the kryptonite ring? [Y/N]')
        while str.upper(take_kryptonite) not in ['Y', 'N']:
            print('Please enter Y or N')
            take_kryptonite = input('Would you like to take the kryptonite ring? [Y/N]')
        if str.upper(take_kryptonite) == 'Y':
            kryptonite -= 1
            gadget_count += 1
            print('You slide the kryptonite ring on your finger')
        elif str.upper(take_kryptonite) == 'N':
            print('You leave the kryptonite ring where it is and continue your journey')
    else:
        print('You have entered the kryptonite containment center')
    direction = input('What direction would you like to travel? [North]')
    while str.upper(direction) != 'NORTH':
        if str.upper(direction) in ['WEST', 'SOUTH', 'EAST']:
            print('There are no rooms in that direction')
            direction = input('What direction would you like to travel? [North]')
        else:
            print('North is the only way to go')
            direction = input('What direction would you like to travel? [North]')
    else:
        print('You travel north')
        crmlb += 1


# Storing the main room function to be called each time a person enters the main room
def main_room():
    # Calling global variables to be updated in this function
    global direction
    global mnrm
    global cstmvlt
    global crmlb
    global tclb
    global trngrm
    mnrm -= 1
    print('You have entered the main room')
    direction = input('What direction would you like to travel? [North, South, East, West]')
    while str.upper(direction) not in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
        direction = input('Please enter North, South, East or West')
    if str.upper(direction) == 'NORTH':
        cstmvlt += 1
        print('You travel north')
    elif str.upper(direction) == 'SOUTH':
        trngrm += 1
        print('You travel south')
    elif str.upper(direction) == 'EAST':
        tclb += 1
        print('You travel east')
    elif str.upper(direction) == 'WEST':
        crmlb += 1
        print('You travel west')


# Storing the hangar function to be called when the player enters the hangar
def hangar():
    # Calling global variables to be updated in this function
    global hngr
    global game_over
    hngr -= 1
    print('You have entered the hangar')
    print('Superman hovers above the ground with glowing red eyes')
    if grapple_gun == 1 or kryptonite == 1 or batarangs == 1 or cure == 1 or smoke_pellets == 1:
        print('Superman lunges at you. You reach for your gadgets but they are missing. You are no match for Superman!')
        game_over = 1
    else:
        print('Superman lunges at you. You quickly react and are able to use your gadgets to administer the cure.')
        game_over = 2


# Print intro to explain the story and the rules
print('The Joker has kidnapped Lois Lane and poisoned Superman with a powerful new toxin that affects the mind.')
print('He has filled Superman''s mind with evil lies about Batman murdering Lois and planning to destroy humanity.')
print('A rage filled, vengeful Superman has crashed through Wayne Manner right into the hangar in the batcave.')
print('Bruce is in the main room of the batcave.  He must first travel north to the costume vault and equipment room.')
print('He will find his batsuit and utility belt to complete his transformation into Batman and start his journey.')
print('To stand a chance against Superman you must find all items before facing him.  Good luck!')


# Loop to ask user when they are ready to start the game
game_start = input('Are you ready to start the game? [Y/N]')
while str.upper(game_start) != 'Y':
    if str.upper(game_start) == 'N':
        game_start = input('Please enter Y when you are ready to start.')
    else:
        game_start = input('Please enter Y or N.')
else:
    print('Welcome to the batcave, Mr. Wayne.  You are currently in the main room.')


# Start tutorial.
# User will be required to go to the north to collect the batsuit and the utility belt before allowing free roam
direction = input('What direction would you like to travel? [North, South, East, West]')
while str.upper(direction) != 'NORTH':
    if str.upper(direction) in ['SOUTH', 'WEST', 'EAST']:
        print('You need to get the batsuit and utility belt to the north before anything else.')
        direction = input('What direction would you like to travel? [North, South, East, West]')
    else:
        direction = input('Please enter North, South, East or West')
else:
    print('You travel north.')


# Arrive in the costume vault and collect the bastsuit before being allowed to continue
costume_vault()
cstmvlt += 1


# User must travel to the east to the equipment room for the utility belt before being allowed to free roam
print('Now you need the utility belt to the east.')
direction = input('What direction would you like to travel? [South, East]')
while str.upper(direction) != 'EAST':
    if str.upper(direction) in ['NORTH', 'WEST']:
        print('There are no rooms in that direction.')
        direction = input('What direction would you like to travel? [South, East]')
    elif str.upper(direction) == 'SOUTH':
        print('You need the utility belt to the east first.')
        direction = input('What direction would you like to travel? [South, East]')
    else:
        direction = input('Please enter South, or East')
else:
    print('You travel east.')


# User must collect the utility belt which will enable free roam
equipment_room()


# End tutorial and start free roam
# While loop that allows users to navigate through rooms as long as the game_over variable is 0.
while game_over == 0:
    if mnrm == 1:
        main_room()
    elif crmlb == 1:
        crime_lab()
    elif cstmvlt == 1:
        costume_vault()
    elif eqmtrm == 1:
        equipment_room()
    elif trngrm == 1:
        training_room()
    elif mdby == 1:
        medical_bay()
    elif tclb == 1:
        technology_lab()
    elif krptvlt == 1:
        kryptonite_vault()
    elif hngr == 1:
        hangar()
else:
    if game_over == 1:
        print('Superman was unable to be stopped!  You Lose!')
        print('Items found:', str(gadget_count) + '/7')
    elif game_over == 2:
        print('Superman was cured!  You Win!')
        print('Items found: 7/7')

