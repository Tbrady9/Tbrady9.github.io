
# Defining the intro to the game
def intro_story():
    print()
    print('           /|                    /|   |\\                   |\\')
    print('         /   \\                  / |___| \\                 /   \\')
    print('       /      \\        /\\      /         \\      /\\       /      \\')
    print('     /          \\     /  \\     |         |     /  \\    /          \\')
    print('    /             \\__/    \\___/           \\___/    \\__/             \\')
    print('   |                                                                 |')
    print('   |               __      ___             ___      __               |')
    print('    \\             /  \\    /    \\          /   \\    /   \\            /')
    print('     \\          /     \\  /      \\        /     \\  /      \\        /')
    print('       \\      /        \\/         \\    /        \\/         \\     /')
    print('         \\   /                     \\  /                     \\  /')
    print('           \\|                       \\/                       |/')
    print()
    print('-----------------------------------------------------------------------------------------------------------')
    print('The Joker has kidnapped Lois Lane and poisoned Superman with a powerful new toxin that affects the mind.')
    print('He has filled Superman''s mind with evil lies about Batman murdering Lois and planning to destroy humanity.')
    print('A rage filled, vengeful Superman has crashed through Wayne Manner right into the hangar in the batcave.')
    print('You are currently in the main room near the middle of the cave.')
    print('To stand a chance against Superman you must find all 7 items before facing him.')
    print('Find all of the items then travel to the Hangar to lure Superman to a trap and cure him')
    print('-----------------------------------------------------------------------------------------------------------')
    print()
    game_mode = input('Please choose a number for your difficulty level:\n'
                      '1 = Easy (Superman will stay in the Hangar and wait for you)\n'
                      '2 = Hard (Superman will roam around. Avoid him and get all items.'
                      'Then find Superman or travel to the Hangar')
    return game_mode


# defining the displayable map
def game_map():
    print('                       --------------------   --------------------')
    print('                       |  Costume Vault   |---|  Equipment Room  |')
    print('                       |                  |   |      Item:       |')
    print('                       |  Item: Batsuit   |---|   Utility Belt   |')
    print('                       --------------------   --------------------')
    print('                             |     |                 |     |      ')
    print('--------------------   --------------------   --------------------')
    print('|    Crime Lab     |---|                  |---|  Technology Lab  |')
    print('|                  |   |     Main Room    |   |                  |')
    print('| Item: Grapple Gun|---|                  |---|Item: Smoke Pellet|')
    print('--------------------   --------------------   --------------------')
    print('      |     |                |     |                 |     |      ')
    print('--------------------   --------------------   --------------------')
    print('| Kryptonite Vault |---|   Training Room  |---|   Medical Bay    |')
    print('|      Item:       |   |                  |   |                  |')
    print('| Kryptonite Ring  |---|  Item: Batarangs |---|   Item: Cure     |')
    print('--------------------   --------------------   --------------------')
    print('                             |     |')
    print('                       --------------------')
    print('                       |                  |')
    print('                       |      Hangar      |')
    print('                       |                  |')
    print('                       --------------------')
