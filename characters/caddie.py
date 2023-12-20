"""This file describes the heroic adventurer Warlock1.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Caddie"
player_name = ""

# Be sure to list Primary class first
classes = ["Warlock"]  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3]  # ex: [10] or [3, 2]
subclasses = ["Hexblade"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Gladiator"
race = "Human"
alignment = "Chaotic good"

age = "21"
height = "164cm"
weight = "72kg"
eyes = "Blue/Green"
skin = "Pale"
hair = "Red"

xp = 900
hp_max = 0
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 10
dexterity = 13
constitution = 16
intelligence = 10
wisdom = 12
charisma = 16

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ("acrobatics", "performance", "deception", "intimidation")

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = (
    "agonizing blast",
    "fiendish vigor",
)

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ("pact of the chain",)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Orc"""

# Inventory
cp = 0
sp = 0
ep = 0
gp = 15
pp = 0

weapons = ("light crossbow", "sling", "dagger")  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "leather armor"  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """- Costume clothes\n
- Love letter of an admirer\n
- Scholar's pack:\n
    - Backpack\n
    - Book of lore\n
    - Bottle of ink\n
    - Ink pen\n
    - 10 sheets of parchment\n
    - Little bag of sand\n
    - Small knife\n
- Light crossbow\n
- Sling\n
- Two daggers\n
- Leather armor\n
- Net\n
"""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = (
    "eldritch blast",
    "friends",
    "armor of agathys",
    "hellish rebuke",
    "witch bolt",
    "suggestion",
)

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = """"""

ideals = """"""

bonds = """"""

flaws = """
"""

features_and_traits = """"""

faction_name = "Topaz:"
portrait = "caddie.png"
symbol = "pseudodragon.jpg"

images = []
