dungeonsheets_version = "0.9.4"

name = "Virgilius Goldriver"
player_name = ""

# Be sure to list Primary class first
classes = ["Bard"]  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3]  # ex: [10] or [3, 2]
subclasses = ["College of Lore"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Noble"
race = "Human"
alignment = "Chaotic good"

age = "27"
height = "178cm"
weight = "79kg"
eyes = "Blue/Brown"
skin = "Tanned"
hair = "Goldish Brown"

xp = 900
hp_max = 0
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 10
dexterity = 16
constitution = 14
intelligence = 11
wisdom = 10
charisma = 16

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = (
    "history",
    "persuasion",
    "sleight of hand",
    "performance",
    "deception",
    "acrobatics",
    "intimidation",
    "stealth",
)

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ("persuasion", "performance")

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerers, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Dwarvish, Gnomish"""

# Inventory
cp = 0
sp = 0
ep = 0
gp = 25
pp = 0

weapons = ("rapier",)  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "leather armor"  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """-Fine clothes\n
-Signet ring\n
-Scroll of pedigree\n
-Diplomat's pack:\n
    -Chest\n
    -2 cases for maps and scrolls\n
    -Fine clothes\n
    -Bottle of ink\n
    -Ink pen\n
    -Lamp\n
    -2 flasks of oil\n
    -5 sheets of paper\n
    -Vial of perfume\n
    -Sealing wax\n
    -Soap\n
-Lute\n
-Rapier\n
-Dagger\n
-Leather armor\n
"""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = (
    "minor illusion",
    "mage hand",
    "command",
    "healing word",
    "silvery barbs",
    "sleep",
    "phantasmal force",
    "shatter",
)

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Backstory
# Describe your backstory here
personality_traits = """I am arrogant, but charming (and extremely good looking).
I am a perfectionist with high standards for myself and others.
I enjoy leaving a lasting impression.
Occasionally I can be overly dramatic.
"""

ideals = """Music and talent can be neither rushed, nor suppressed.
I play my music not due to some minor desire for entertainment,
but because it demands to be played.
The world deserves my beauty.
"""

bonds = """I have strained relationship with my father.
He never approved of my music, and I never approved of his politics.
He is the reason I left home and don't like to discuss my origins.
Even though we are not on speaking terms,
I still care for him and my mother."""

flaws = """I find it difficult to form lasting emotional connections.
I desire recognition and validation, which explains my competitive nature.
"""

features_and_traits = """"""

backstory = """"""

allies = """The Goldriver family controls a trading empire of notable size and likes to take political influence.
"""
faction_name = "Goldriver emblem:"

portrait = "virgilius_goldriver.png"
symbol = "goldriver_emblem.png"

images = []
