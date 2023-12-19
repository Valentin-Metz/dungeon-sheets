dungeonsheets_version = "0.9.4"

name = "Emilia Shadowthorn"
player_name = ""

# Be sure to list Primary class first
classes = ["Ranger"]  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3]  # ex: [10] or [3, 2]
subclasses = ["Beast Master"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Criminal"
race = "Drow"
alignment = "Chaotic neutral"

age = "101"
height = "162cm"
weight = "73kg"
eyes = "Blue"
skin = "Dark grey"
hair = "White"

xp = 900
hp_max = 0
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 8
dexterity = 16
constitution = 10
intelligence = 10
wisdom = 14
charisma = 16

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = (
    "deception",
    "stealth",
    "animal handling",
    "perception",
    "intimidation",
)

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

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
feature_choices = ("archery",)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Elvish, Thieves' Cant, Undercommon"""

# Inventory
cp = 0
sp = 0
ep = 0
gp = 15
pp = 0

weapons = (
    "shortsword",
    "shortsword",
    "light crossbow",
)  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "leather armor"  # Eg "leather armor"
shield = ""  # Eg "shield"

equipment = """- Dark common clothes\n
- Leather armor\n
- Dungeoneer's pack:\n
    - Backpack\n
    - Crowbar\n
    - Hammer\n
    - 10 pitons\n
    - 10 torches\n
    - Tinderbox\n
    - 10 days of rations\n
    - Waterskin\n
    - 50 feet of hempen rope\n
- Two shortswords\n
- Light crossbow\n
"""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = (
    "hunter's mark",
    "hail of thorns",
    "goodberry",
)

# Which spells have not been prepared
__spells_unprepared = ("faerie fire",)

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ("giant wolf spider",)  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here
personality_traits = """Cunning, ruthless, and ambitious.
I have high expectations for myself and others.
I am impressed by true talent, not wealth or social status.
"""

ideals = """Power through chaos. Adapt fast to changing circumstances.
I disdain surface dwellers. Their comforts have made them weak and complacent."""

bonds = """Allegiance to a secret drow society aiming to dominate surface lands.
"""

flaws = """I am overconfidence in my abilities.
I find it difficult to accept help from others.
"""

features_and_traits = """On crit: Apply poison of companion spider."""

backstory = """Born in the dark and treacherous city of Menzoberranzan,
a place where only the strong and cunning survive.
Raised in a powerful drow house,  trained form a young age in the arts of stealth, combat, and deception.
Emilia quickly rose through the ranks due to her merciless nature and exceptional skills as a ranger.

Her loyalty to Lolth, the drow deity of chaos and destruction, is unyielding.
Emilia was involved in numerous plots and assassinations, both within the drow society and against surface dwellers.
Her ultimate goal is to weaken the surface nations, making them ripe for drow domination."""

faction_name = "Tobias:"
allies = """Tobias: A giant wolf spider that Emilia befriended during her training.\n
---Stats---\n
AC: 13\n
HP: 11\n
Speed: 40 ft., climb 40 ft.\n
STR: 12 (+1); DEX: 16 (+3); CON: 12 (+1); INT: 3 (-4); WIS: 12 (+1); CHA: 4 (-3)\n
---Abilities---\n
Spider Climb:\n
The spider can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.

Web Sense:\n
While in contact with a web, the spider knows the exact location of any other creature in contact with the same web.

Web Walker:\n
The spider ignores movement restrictions caused by webbing.

---Actions---\n
Bite:\n
Melee Weapon Attack: +3 to hit, reach 5 ft., one creature.
Hit: 4 (1d6 + 1) piercing damage, and the target must make a DC 11 Constitution saving throw,
taking 7 (2d6) poison damage on a failed save, or half as much damage on a successful one.
If the poison damage reduces the target to 0 hit points, the target is stable but poisoned for 1 hour,
even after regaining hit points, and is paralyzed while poisoned in this way.
"""

other_feats_traits = """Distinguishing features:\n
Intricate spider web tattoo covering her right arm,
signifying her loyalty to Lolth, the drow deity.\n
\n
Favoured enemy: Humanoids & Undead\n
\n
Favoured terrain: Underdark & Mountains
"""

portrait = "emilia_shadowthorn.png"
symbol = "pet_spider.png"

images = []
