# Organizes a single world which a player must
# conquer to move forward in their adventure


class World:
    """
    The World class is created when an adventure is
    created.
    """
    def __init__(self):
        """
        Constructor for the Adventure class
        param: name - string of player name
        returns: new Adventure object
        """
        self.name = 'World 1'
        self.boss = None
        self.underlings = []
