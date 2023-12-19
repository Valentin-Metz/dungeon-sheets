dungeonsheets_version = "0.9.4"

name = "Elitrana Pineth"
player_name = ""

# Be sure to list Primary class first
classes = ["Rogue"]  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3]  # ex: [10] or [3, 2]
subclasses = ["Thief"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Charlatan"
race = "Half-Elf"
alignment = "Chaotic good"

age = "27"
height = "160cm"
weight = "56kg"
eyes = "Blue/Green"
skin = "Pale Ivory"
hair = "Metallic Blue"

xp = 900
hp_max = 0
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 8
dexterity = 16
constitution = 10
intelligence = 16
wisdom = 8
charisma = 16

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = (
    "deception",
    "sleight of hand",
    "acrobatics",
    "athletics",
    "deception",
    "investigation",
    "persuasion",
    "stealth",
)

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ("stealth", "thieves' tools")

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
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
languages = """Common, Elvish, Thieves' Cant, Deep Speech"""

# Inventory
cp = 0
sp = 0
ep = 0
gp = 15
pp = 0

weapons = ("rapier", "dagger", "shortbow")  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "leather armor"  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """-Fine clothes\n
-Disguise kit (p)\n
-Burglar's pack:\n
    - Backpack\n
    - Bag of 1000 ball bearings\n
    - 10 feet of string\n
    - Bell\n
    - 5 candles\n
    - Crowbar\n
    - Hammer\n
    - 10 pitons\n
    - Hooded lantern\n
    - 2 flasks of oil\n
    - 5 days rations\n
    - Tinderbox\n
    - Waterskin\n
    - 50 feet of hempen rope\n
-Thieves' tools (e)\n
-Set of weighted dice\n
-Rapier\n
-Two daggers\n
-Shortbow\n
-Leather armor\n
"""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ()

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = """Elitrana has a guarded nature, and she doesn't easily open up to others.
She's been betrayed in the past,
and it takes time for her to trust someone enough to share her true thoughts and feelings,
but once she establishes a bond of trust, her loyalty is unwavering.
She values the few close relationships she forms and will go to great lengths
to protect and support those she considers true friends."""

ideals = """Elitrana cherishes her freedom above all else.
She believes in the right of individuals to make their own choices and live without undue restrictions.
She may resist authority figures who try to control or limit her actions,
valuing the ability to carve her own path."""

bonds = """Elitrana owes much of her life to the thieves' guild that took her in as a child.
She greatly respects the head of the guild, and she seeks to prove herself worthy of her position.
She hopes to one day pay back the guild for the kindness and generosity
that saved her from a life of poverty and misery."""

flaws = """When faced with stressful situations,
Elitrana tends to chatter nervously and share more information than necessary.
She's also prone to exaggeration and embellishment when relating stories about her exploits.
"""

allies = """"""
faction_name = "Fusel:"

features_and_traits = """"""

portrait = "elitrana_pineth.jpg"
symbol = "fusel.jpg"

images = []
