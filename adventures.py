# Organizes an adventure for a player to embark on


class Adventure:
    """
    The Adventure class is created when a player
    starts a new game. This class keeps track of
    the player's progress through the adventure.
    """
    def __init__(self, player_name):
        """
        Constructor for the Adventure class
        param: player_name - string of player name
        returns: new Adventure object
        """
        self.player_name = player_name
        self.battles_won = 0
        self.bosses_defeated = 0
        self.worlds = {}
