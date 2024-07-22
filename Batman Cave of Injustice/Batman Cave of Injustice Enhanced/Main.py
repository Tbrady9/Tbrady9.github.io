# Batman: Cave of Injustice by Tim Brady

from Resources import *
import random

# Dictionary for rooms that contains movement and item possibilities
rooms = {
    'Main Room': {'South': 'Training Room', 'North': 'Costume Vault', 'East': 'Technology Lab', 'West': 'Crime Lab'},
    'Costume Vault': {'South': 'Main Room', 'East': 'Equipment Room', 'Item': 'Batsuit'},
    'Equipment Room': {'West': 'Costume Vault', 'South': 'Technology Lab', 'Item': 'Utility Belt'},
    'Crime Lab': {'South': 'Kryptonite Vault', 'East': 'Main Room', 'Item': 'Grapple Gun'},
    'Kryptonite Vault': {'North': 'Crime Lab', 'East': 'Training Room', 'Item': 'Kryptonite Ring'},
    'Technology Lab': {'South': 'Medical Bay', 'West': 'Main Room', 'North': 'Equipment Room', 'Item': 'Smoke Pellets'},
    'Training Room': {'North': 'Main Room', 'South': 'Hangar', 'East': 'Medical Bay', 'West': 'Kryptonite Vault',
                      'Item': 'Batarangs'},
    'Medical Bay': {'North': 'Technology Lab', 'West': 'Training Room', 'Item': 'Cure'},
    'Hangar': {'North': 'Training Room'}
}

# List of possible directions for random Superman movement
s_movements = ['North', 'South', 'East', 'West']

# Intro
# Displays the intro from Resources.py and prompts the user to select a difficulty
# Input: None - Output: None
game_mode = intro_story()
print()
if game_mode == '1':
    print('You have chosen the easy difficulty\n'
          'Superman will stay put in the Hangar')
else:
    print('You have chosen the hard difficulty\n'
          'Avoid Superman as he searches for you')
print()


# Player start location and direction
location = 'Main Room'
direction = ''
# Superman start location and direction
s_location = 'Hangar'
s_direction = ''


# gameover variable (0 while playing, 1 to quit, 2 and 4 to end game with loss, 3 and 5 to end game with win)
gameover = 0


# Location update
# Updates the location based on the associated location and direction in the 'rooms' dictionary
# Input: location, direction - Output: new room location
def get_new_room(location, direction):
    new_room = location
    for i in rooms:
        if i == location:
            if direction in rooms[i]:
                new_room = rooms[i][direction]
    return new_room


# Item retrieval function
def get_item(location):
    return rooms[location]['Item']


# Item list
item_list = ['Batsuit', 'Utility Belt', 'Grapple Gun', 'Smoke Pellets', 'Batarangs', 'Cure', 'Kryptonite Ring']

# Open list of items retrieved that will have items added to it as they are picked up
items_retrieved = []


# View inventory
# Allows the user to display a list of collected inventory
# Input: None - Output: items_retrieved array (item list)
def view_inventory():
    print()
    print('---------------------')
    print('|  Collected Items  |')
    print('---------------------')
    if len(items_retrieved) == 0:
        print('  ', 'None')
    else:
        for i in items_retrieved:
            print('  ', i)


# Main game loop to continuously prompt user for direction until game over or exit
while gameover == 0:

    # Notify user of their location
    print('You are in the', location)
    print('Superman is in the', s_location)
    print()

    # Prompt item retrieval in rooms that have items
    if location not in ['Main Room', 'Hangar']:
        item = get_item(location)

        # Check that item has not been retrieved already
        if item not in items_retrieved:
            collect = input('You see the ' + item + '. Would you like to collect it? [Y/N]')
            print('-----------------')
            collect = collect.capitalize()

            # Input validation
            while collect not in ['Y', 'N']:
                collect = input('Please enter a valid selection [Y/N]')
                collect = collect.capitalize()

            # Collect or leave the item
            else:
                if collect == 'Y':
                    items_retrieved.append(item)
                    print('You have collected the ' + item)
                elif collect == 'N':
                    print('You have chosen to leave the ' + item)

    # Prompt the user for input (direction to travel, exit, map, or inventory)
    direction = input('Enter a direction to travel [North, South, East, West]\n'
                      'You can also \'Exit\' to quit the game, \'M\' to view the map, \'I\' to view inventory')
    print('-----------------')
    direction = direction.capitalize()
    s_direction = random.choice(s_movements)

    # Input validation
    while direction not in ('North', 'South', 'East', 'West', 'Exit', 'M', 'I'):
        direction = input('Please choose a valid option [North, South, East, West, Exit, M, I]')
        direction = direction.capitalize()

    # Input choices that are not directions to travel
    else:
        if direction == 'Exit':
            gameover = 1
        elif direction == 'M':
            game_map()
        elif direction == 'I':
            view_inventory()
            print()

        # Update the user's location based on their direction travelled
        # Also randomly updates Superman's location
        # If no room exists in that direction, Superman does not move
        else:
            new_room = get_new_room(location, direction)
            s_new_room = get_new_room(s_location, s_direction)
            if new_room == location:
                print('There is no room in that direction')

            # prompting the user with a warning if they enter the hangar without all items.
            # Users can continue on for a loss or choose another direction
            elif new_room == 'Hangar':
                if len(items_retrieved) < 7:
                    print('You hear Superman\'s destruction in the next room.')
                    print('You are unprepared for the fight that lies ahead.')
                    go_on = input('Are you sure you want to continue south? [Y/N]')
                    print('-----------------')
                    go_on = go_on.capitalize()

                    # If user continues on, game over with loss
                    if go_on == 'Y':
                        gameover = 2

                    # Input validation
                    elif go_on != 'N':
                        go_on = input('Please enter a valid selection [Y/N]')

                # User enters the Hangar with all items in possession
                # Game over with win
                else:
                    gameover = 3

            # Update user and Superman locations
            else:
                location = new_room
                if game_mode == '2':
                    s_location = s_new_room

                    # If new locations for user and Superman are the same on hard mode
                    # All items = game over with win, <7 items = game over with loss
                    if (location == s_location) and (game_mode == '2'):
                        if len(items_retrieved) != 7:
                            gameover = 4
                        else:
                            gameover = 5

# Possible game over outcomes
else:
    # User quits
    if gameover == 1:
        print('You have chosen to quit')
        print('Thank you for playing!')

    # User advances to the end (Hangar) without all items (loss)
    elif gameover == 2:
        print('***********************')
        print('You enter the Hangar and see Superman')
        print('You tried to fight Superman with', len(items_retrieved), 'out of 7 items')
        print('Without all of your items you were no match')
        print('You Lose')
        print('***********************')

    # User advances to the end (Hangar) with all items (win)
    elif gameover == 3:
        print('***********************')
        print('You enter the Hangar and see Superman')
        print('The fight between you and Superman was a tough one')
        print('Using all 7 of the items that you collected, you were able to administer the cure')
        print('You Win!')
        print('***********************')

    # User location = Superman location without all items (loss)
    elif gameover == 4:
        print('***********************')
        print('Superman has caught you in the', location + '. You are unprepared for the fight')
        print('You lose')
        print('***********************')
    # User location = Superman location with all items (win)

    elif gameover == 5:
        print('***********************')
        print('Superman has caught you in the', location + '. You managed to find all 7 items')
        print('Using all 7 of the items that you collected, you were able to administer the cure')
        print('You Win!')
        print('***********************')
