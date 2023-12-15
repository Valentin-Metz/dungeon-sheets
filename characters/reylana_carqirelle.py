dungeonsheets_version = "0.9.4"

name = "Reylana Carquirelle"
player_name = ""

# Be sure to list Primary class first
classes = ["Druid"]  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3]  # ex: [10] or [3, 2]
subclasses = ["Circle of the Land"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Hermit"
race = "Wood Elf"
alignment = "Lawful good"

age = "219"
height = "153cm"
weight = "53kg"
eyes = "Brown"
skin = "Bright with a slight tan"
hair = "Turquoise"

xp = 900
hp_max = 0
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 8
dexterity = 16
constitution = 13
intelligence = 10
wisdom = 16
charisma = 12

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ("perception", "medicine", "religion", "insight", "survival")

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

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
feature_choices = ("forest",)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Elvish, Druidic, Sylvan"""

# Inventory
cp = 0
sp = 0
ep = 0
gp = 5
pp = 0

weapons = "scimitar"  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "leather armor"  # Eg "leather armor"
shield = "wooden shield"  # Eg "shield"

equipment = """- Explorer's pack\n
- Druidic focus\n
(Yew wand)\n
- Herbalism kit\n
- Common clothes\n
- Winter blanket\n
- A scroll case stuffed full of notes from your studies or prayers\n
"""

attacks_and_spellcasting = ""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = (
    "mending",
    "produce flame",
    "guidance",
    "speak with animals",
    "healing word",
    "thunderwave",
    "animal messenger",
    "pass without trace",
    "hold person",
)

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

wild_shapes = [
    "cat",
    "badger",
    "boar",
    "deer",
    "draft horse",
    "giant badger",
    "giant lizard",
    "giant rat",
    "goat",
    "mastiff",
    "mule",
    "lizard",
    "pony",
    "rat",
    "riding horse",
    "spider",
    "weasel",
    "wolf",
]

# Backstory
# Describe your backstory here
personality_traits = """Despite her age, she maintains a childlike sense of wonder and curiosity.
She's always eager to explore and discover new things, whether it's a rare flower or a hidden animal den."""

ideals = """In a world filled with challenges and darkness,
Reylana values the power of laughter and light-heartedness.
She believes that maintaining a positive outlook
and finding humor in the midst of adversity can be a source of strength."""

bonds = """She has formed strong bonds with her fellow adventurers.
They've become a tight-knit group, and she considers them not just comrades in arms but true friends.
Their well-being is a top priority for her."""

flaws = """Reylana has an aversion to causing harm, even to enemies.
Her stubborn idealism and optimistic wordview can be a source of frustration for her companions.
"""

allies = """Bond with Frisk (Squirrel):

Frisk, the playful and nimble squirrel,
has been a constant companion to Reylana since her early days in the forest.
The bond between them is one of pure joy and mischief.
Frisk, with its soft fur and quick movements, is the embodiment of Reylanas playful curiosity.
The squirrel often scampers ahead on their woodland adventures,
discovering hidden nuts, mimicking her mischievous nature with acrobatic leaps,
and occasionally stealing small trinkets just for the fun of it.

Despite their differences in size, Reylana and Frisk share an unspoken understanding.
Frisk is not just a companion; it's a friend who brings laughter to the darkest moments
and a source of comfort during lonely nights beneath the forest canopy.
The squirrel's presence is a reminder of the simple joys found in the heart of nature.



Bond with Rebecca (Falcon):

Rebecca, the majestic falcon, is the soaring spirit of the skies that Reylana shares an intricate bond with.
They met when she was wandering through a dense thicket,
and a magnificent falcon swooped down from the heavens to perch on her outstretched arm.
Since that fateful encounter, Rebecca has become a loyal and trusted ally.

Rebecca is the keen-eyed guardian of the skies, serving as both scout and companion.
With a regal presence and a sharp intellect,
the falcon and Reylana communicate through subtle gestures and shared instincts.
Whether it's tracking elusive prey, scouting dangerous territories, or simply reveling in the freedom of flight,
Rebecca is a constant presence, providing a sense of awe and wonder as they navigate the realms together.

The bond with Rebecca extends beyond the physical, transcending the boundaries between elf and falcon.
In moments of meditation, Reylana can feel the rush of wind beneath Rebecca's wings
and witness the breathtaking landscapes from her aerial perspective.
The falcon is not just a companion; she is a reflection of the untamed spirit of the wilderness,
soaring beside Reylana as they both embrace the boundless beauty of the natural world."""
faction_name = "Frisk:"

features_and_traits = """"""

other_feats_traits = """Whispers of the Wind:

As she moves through the forest, a subtle rustle follows in her wake,
leaves and grasses seemingly parting in acknowledgment of her presence.
It's as if the very air and flora respond to her, recognizing the daughter of the woods.



Eyes of the Owl:

Her eyes, resembling the keen gaze of an owl, betray an otherworldly wisdom.
In moments of concentration or deep contemplation, they gleam with an ancient knowing,
a glimpse into the timeless secrets held within the heart of the wilderness.



Nature's Embrace:

A soft aura of natural tranquility surrounds her, a gentle caress of calmness that soothes both friend and foe alike.
It's as if the very essence of the forest itself embraces her,
creating an aura of peace and serenity wherever she goes."""

treasure = """A delicate talisman crafted from intertwined vines and adorned with vibrant flowers.
This magical amulet enhances her connection to the natural world,
providing a subtle boost to her druidic abilities
and serving as a symbol of her commitment to preserving the balance of the forest."""

portrait = "reylana_carqirelle.jpg"
symbol = "squirrel.jpg"

images = []
