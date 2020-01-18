# List of Enemies to go against

DRAFTED = []
DEFEATED = []
CHALLENGED = []

ENEMIES = (
    "Lucifer",
    "Lot",
    "Jacob",
    "Esau",
    "Bathsheba",
    "Delilah",
    "Joab",
    "James",
    "Judas",
    "Isaiah",
    "Daniel",
    "Xerxes",
    "Jeremiah",
    "Nehemiah",
    "Job",
    "Elihu",
    "Uriah",
    "Dorcas",
    "Rhoda",
    "Elisha",
    "Jezebel",
    "Ahab",
    "Amnon",
    "Tamar",
    "Absalom",
    "Nathan",
    "Boaz",
    "Ruth",
    "Joseph",
    "Simeon",
    "Benjamin",
    "Nebuchadnezzar",
    "Methusaleh",
    "Mary",
    "Mary Magdalene",
    "Abraham",
    "Sarah",
    "Rebekah",
    "Rahab",
    "Joshua",
    "Adam",
    "Eve",
    "Satan",
    "Gabriel",
    "Hosea",
    "Gomer",
    "Ezekiel",
    "Matthew",
    "Solomon",
    "Joash",
    "Aaron",
    "Miriam",
    "Potiphar",
    "Isaac",
    "Noah",
    "Ham",
    "Shem",
    "Japheth",
    "Zechariah",
    "John the Baptist",
    "Hezekiah",
    "Paul",
    "Saul",
    "Esther",
    "Mordecai",
    "Darius",
    "Shadrach",
    "Meshach",
    "Abednego",
    "Jeroboam",
    "Rehoboam",
    "Samuel",
    "Samson",
    "Barak",
    "Balaam",
    "Herod",
    "Martha",
    "Lazarus",
    "Zacheus"
)

POKEDEX = {
    "Lucifer": {
        "bio": "a beautiful fallen angel",
        "righteous": "0",
        "strength": "9"
    },
    "Lot": {
        "bio": "nephew of Abraham",
        "righteous": "3",
        "strength": "2"
    },
    "Jacob": {
        "bio": "wrestled with God",
        "righteous": "5",
        "strength": "5"
    },
    "Esau": {
        "bio": "father of Edom",
        "righteous": "3",
        "strength": "5"
    },
    "Bathsheba": {
        "bio": "mother of Solomon",
        "righteous": "4",
        "strength": "4"
    },
    "Delilah": {
        "bio": "killer of men",
        "righteous": "0",
        "strength": "2"
    },
    "Joab": {
        "bio": "killer of men",
        "righteous": "2",
        "strength": "5"
    },
    "James": {
        "bio": "brother of Jesus",
        "righteous": "5",
        "strength": "3"
    },
    "Judas": {
        "bio": "betrayer of Jesus",
        "righteous": "1",
        "strength": "2"
    },
    "Isaiah": {
        "bio": "a great prophet",
        "righteous": "7",
        "strength": "2"
    },
    "Daniel": {
        "bio": "exile prophet",
        "righteous": "7",
        "strength": "3"
    },
    "Xerxes": {
        "bio": "king to Esther",
        "righteous": "2",
        "strength": "5"
    },
    "Jeremiah": {
        "bio": "author of Lamentations",
        "righteous": "7",
        "strength": "3"
    },
    "Nehemiah": {
        "bio": "builder of walls",
        "righteous": "6",
        "strength": "5"
    },
    "Job": {
        "bio": "afflicted",
        "righteous": "6",
        "strength": "6"
    },
    "Elihu": {
        "bio": "friend of Job",
        "righteous": "4",
        "strength": "2"
    },
    "Uriah": {
        "bio": "I just feel bad for this guy",
        "righteous": "5",
        "strength": "5"
    },
    "Dorcas": {
        "bio": "friend to the poor",
        "righteous": "5",
        "strength": "3"
    },
    "Rhoda": {
        "bio": "daughter of the gospel",
        "righteous": "4",
        "strength": "4"
    },
    "Elisha": {
        "bio": "apprentice to Elijah",
        "righteous": "3",
        "strength": "2"
    },
    "Jezebel": {
        "bio": "wicked queen",
        "righteous": "0",
        "strength": "4"
    },
    "Ahab": {
        "bio": "foolish king",
        "righteous": "1",
        "strength": "3"
    },
    "Amnon": {
        "bio": "bad dude",
        "righteous": "0",
        "strength": "2"
    },
    "Tamar": {
        "bio": "I just feel bad for her",
        "righteous": "5",
        "strength": "5"
    },
    "Absalom": {
        "bio": "foolish prince",
        "righteous": "1",
        "strength": "3"
    },
    "Nathan": {
        "bio": "David's conscience",
        "righteous": "5",
        "strength": "3"
    },
    "Boaz": {
        "bio": "husband to Ruth",
        "righteous": "5",
        "strength": "4"
    },
    "Ruth": {
        "bio": "awesome convert",
        "righteous": "5",
        "strength": "2"
    },
    "Joseph": {
        "bio": "great visionary",
        "righteous": "6",
        "strength": "5"
    },
    "Simeon": {
        "bio": "mean brother to Joseph",
        "righteous": "2",
        "strength": "2"
    },
    "Benjamin": {
        "bio": "younger brother to Joseph",
        "righteous": "3",
        "strength": "3"
    },
    "Nebuchadnezzar": {
        "bio": "King of Babylon",
        "righteous": "3",
        "strength": "5"
    },
    "Methusaleh": {
        "bio": "oldest man",
        "righteous": "4",
        "strength": "5"
    },
    "Mary": {
        "bio": "mother of Jesus",
        "righteous": "5",
        "strength": "3"
    },
    "Mary Magdalene": {
        "bio": "forgiven",
        "righteous": "6",
        "strength": "2"
    },
    "Abraham": {
        "bio": "father of a nation",
        "righteous": "6",
        "strength": "3"
    },
    "Sarah": {
        "bio": "wife to Abraham",
        "righteous": "3",
        "strength": "2"
    },
    "Rebekah": {
        "bio": "mother of Jacob and Esau",
        "righteous": "3",
        "strength": "3"
    },
    "Rahab": {
        "bio": "Jericho convert",
        "righteous": "5",
        "strength": "3"
    },
    "Joshua": {
        "bio": "apprentice to Moses",
        "righteous": "5",
        "strength": "5"
    },
    "Adam": {
        "bio": "first man",
        "righteous": "5",
        "strength": "6"
    },
    "Eve": {
        "bio": "first woman",
        "righteous": "5",
        "strength": "5"
    },
    "Satan": {
        "bio": "the dark side",
        "righteous": "0",
        "strength": "8"
    },
    "Gabriel": {
        "bio": "angel of light",
        "righteous": "9",
        "strength": "9"
    },
    "Hosea": {
        "bio": "faithful prophet",
        "righteous": "5",
        "strength": "4"
    },
    "Gomer": {
        "bio": "not a good wife",
        "righteous": "1",
        "strength": "1"
    },
    "Ezekiel": {
        "bio": "saw God",
        "righteous": "6",
        "strength": "2"
    },
    "Matthew": {
        "bio": "tax collector disciple",
        "righteous": "4",
        "strength": "2"
    },
    "Solomon": {
        "bio": "wisest man with a past",
        "righteous": "3",
        "strength": "2"
    },
    "Joash": {
        "bio": "young king, tragic backstory",
        "righteous": "2",
        "strength": "2"
    },
    "Aaron": {
        "bio": "first Israel priest",
        "righteous": "4",
        "strength": "2"
    },
    "Miriam": {
        "bio": "sister of Moses",
        "righteous": "3",
        "strength": "2"
    },
    "Potiphar": {
        "bio": "believed his wife",
        "righteous": "1",
        "strength": "1"
    },
    "Isaac": {
        "bio": "the prophesied son",
        "righteous": "4",
        "strength": "4"
    },
    "Noah": {
        "bio": "built an ark",
        "righteous": "6",
        "strength": "5"
    },
    "Ham": {
        "bio": "cursed son of Noah",
        "righteous": "1",
        "strength": "3"
    },
    "Shem": {
        "bio": "son of Noah",
        "righteous": "3",
        "strength": "3"
    },
    "Japheth": {
        "bio": "son of Noah",
        "righteous": "3",
        "strength": "3"
    },
    "Zechariah": {
        "bio": "father of John the Baptist",
        "righteous": "3",
        "strength": "2"
    },
    "John the Baptist": {
        "bio": "the new coming of Isaiah",
        "righteous": "8",
        "strength": "2"
    },
    "Hezekiah": {
        "bio": "asked for more life... got 15 years",
        "righteous": "4",
        "strength": "2"
    },
    "Paul": {
        "bio": "brought people to Christ",
        "righteous": "7",
        "strength": "4"
    },
    "Saul": {
        "bio": "killed followers of Christ",
        "righteous": "1",
        "strength": "3"
    },
    "Esther": {
        "bio": "the most beautiful queen",
        "righteous": "5",
        "strength": "5"
    },
    "Mordecai": {
        "bio": "uncle of Esther",
        "righteous": "5",
        "strength": "1"
    },
    "Darius": {
        "bio": "sent Daniel to the lions den",
        "righteous": "3",
        "strength": "4"
    },
    "Shadrach": {
        "bio": "friend of Daniel",
        "righteous": "4",
        "strength": "4"
    },
    "Meshach": {
        "bio": "friend of Daniel",
        "righteous": "4",
        "strength": "4"
    },
    "Abednego": {
        "bio": "friend of Daniel",
        "righteous": "4",
        "strength": "4"
    },
    "Jeroboam": {
        "bio": "could've had the kingdom",
        "righteous": "2",
        "strength": "4"
    },
    "Rehoboam": {
        "bio": "listened to young ones instead of the wiser elders",
        "righteous": "1",
        "strength": "2"
    },
    "Samuel": {
        "bio": "told off the priest",
        "righteous": "7",
        "strength": "4"
    },
    "Samson": {
        "bio": "the strongest man but wasted potential",
        "righteous": "4",
        "strength": "8"
    },
    "Barak": {
        "bio": "fought alongside Deborah",
        "righteous": "5",
        "strength": "6"
    },
    "Balaam": {
        "bio": "talked to a donkey",
        "righteous": "2",
        "strength": "1"
    },
    "Herod": {
        "bio": "tried to kill Jesus",
        "righteous": "0",
        "strength": "6"
    },
    "Martha": {
        "bio": "sister to Lazarus",
        "righteous": "5",
        "strength": "2"
    },
    "Lazarus": {
        "bio": "raised from the dead",
        "righteous": "5",
        "strength": "3"
    },
    "Zacheus": {
        "bio": "climbed a tree to talk to Jesus",
        "righteous": "4",
        "strength": "2"
    },
}
