# The beginning of the game

import time

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
    """

    champion_id = int(raw_input("Enter the champions number: "))

    if champion_id == 1:
        print "You have selected wisely. Your champion is Moses."
    elif champion_id == 2:
        print "Your choice is strong. Your champion is King David."
    elif champion_id == 3:
        print "Your champion is Simon Peter."
    else:
        champion_id = -1

print "Now to find your opponent."

exit = True
while exit:
    player_input = str(raw_input("777: "))
    if player_input == "exit":
        exit = False

if not exit:
    print "\n\nShutting down the game."
    time.sleep(3)
