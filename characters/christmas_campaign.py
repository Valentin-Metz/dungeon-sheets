from dungeonsheets import mechanics


# This line (or one like it) is required in order for dungeonsheets to
# recognize the file.
dungeonsheets_version = "0.17.0"

# Specifying ``sheet_type = "gm"`` gives us GM notes instead of a
# player character sheet.
sheet_type = "gm"

# A short description of what happened last time, etc.
summary = """The characters need to find Astronomy Professor Eulertin a top a snowy mountain.
"""

party = [
    "rogue/elitrana_pineth/elitrana_pineth.py",
    "ranger/emilia_shadowthorn/emilia_shadowthorn.py",
    "druid/reylana_carquirelle/reylana_carquirelle.py",
    "bard/virgilius_goldriver/virgilius_goldriver.py",
]

# A descriptive title to appear at the top of the document.
session_title = "Christmas Campaign"

# Dungeonsheets supports a rudimentary version of cascading sheets. In
# this case, details for the whole campaign can be defined once, then
# sheets can be generated for each specific session using the
# *parent_sheets* attribute.
parent_sheets = []

# Defining a *monsters* attribute will include their stat blocks in
# the output
monsters = [
    "wraith",
    "sword wraith warrior",
    "air elemental",
    "kobold",
    "banshee",
    "manticore",
    "zombie",
]

# Arbitrary sections can be added to the GM notes. The
# ``extra_sections`` attribute should be a sequence of subclasses of
# the *Content* base class. For each entry in the sequence, the *name*
# attribute will be used for the section title, and the docstring will
# make up the body


extra_content = []
