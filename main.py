# The beginning of the game

import time
import random

from enemies import ENEMIES, DEFEATED, CHALLENGED


def is_player_closest(original, player, enemy):
    """
    Return True if the player is closer in number
    to the original than the enemy.
    """
    player_difference = abs(original - player)
    enemy_difference = abs(original - enemy)
    if player_difference < enemy_difference:
        return True
    return False


print """
Welcome to Bible Heroes Challenge!\n
You will pit your favorite Bible heroes
against one another in a tournament of
epic proportions.
\n
"""

player_name = str(raw_input("Enter your name: "))

print "It is a pleasure to meet you %s" % player_name

champion_id = -1

while champion_id == -1:
    print """
    Choose one of the following champions:
    1: Moses
    2: King David
    3: Simon Peter
    4: Deborah
    """

    champion_id = int(raw_input("Enter the champions number: "))

    if champion_id == 1:
        print "You have selected wisely. Your champion is Moses."
    elif champion_id == 2:
        print "Your choice is strong. Your champion is King David."
    elif champion_id == 3:
        print "Your champion is Simon Peter."
    elif champion_id == 4:
        print "A warrior judge. Your champion is Deborah."
    else:
        champion_id = -1

print "Now to find your opponent."

exit = True
while exit:
    player_input = str(raw_input("777: "))
    if player_input == "exit":
        exit = False
    elif player_input == "wins":
        print DEFEATED
    elif player_input == "fight":
        print "\nSelecting enemy."
        time.sleep(1)
        selected_enemy_name = None
        while selected_enemy_name == None:
            selected_enemy_index = random.randrange(0, len(ENEMIES))
            if ENEMIES[selected_enemy_index] in CHALLENGED:
                continue
            selected_enemy_name = ENEMIES[selected_enemy_index]
        print "You have challenged %s" % selected_enemy_name
        print "\nReady..."
        time.sleep(1)
        print "BATTLE!!!"
        battle_random_number = random.randrange(1, 21)
        player_battle_number_input = int(raw_input("Pick a number between 1 and 20: "))
        enemy_battle_number_input = random.randrange(1, 21)
        print "\nYou chose %s" % player_battle_number_input
        print "Calculating..."
        time.sleep(1)
        if is_player_closest(battle_random_number, player_battle_number_input, enemy_battle_number_input):
            print "You win"
            DEFEATED.append(selected_enemy_name)
        else:
            print "%s WINS" % selected_enemy_name
        CHALLENGED.append(selected_enemy_name)


if not exit:
    print "\n\nShutting down the game."
    time.sleep(3)
