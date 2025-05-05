class File:
    def __init__(self, name, files=None):
        self.name = name
        self.files = files
        self.is_dir = files is not None

# Nested structure representing a directory hierarchy
# Note how a directory is made from File class
my_dir = File('root', files=[
    File('almonds', files=[
        File('default', files=[
            File('fortune')
        ]),
        File('explore', files=[
            File('gateway')
        ])
    ]),
    File('blanket', files=[
        File('harvest'),
        File('journey', files=[])
    ]),
    File('capture')
])

# Each "file" dict has the following attributes:
# name: (str) the name of the file
# is_dir: (bool) whether this file is a directory
# files: (list) a list of the files in the directory
#               None if this file is not directory

# The equivalent structure: We can actually make it in our project Dir;
# In Homebrew: $ install Tree then in terminal you can use the follwoing 
# command $ tree <Root folder> then we can see the graphic of our directory
# here jourmey is folder the rest are files.

# root
# ├── almonds
# │   ├── default
# │   │   └── fortune
# │   └── explore
# │       └── gateway
# ├── blanket
# │   ├── harvest
# │   └── journey (dir, but empty)
# └── capture

# Write a recursive function to print just the files (non directories)
def print_files(file):
    # what's the recursive case?
    # what's the base case (how do we know to stop recursing)?
    # when should we print?
    if not file.is_dir:
        print(file.name)
    else:
        # it is a directory
        # check each of the child files
        for child in file.files:
            print_files(child)    


print("== print_files ==")
print_files(my_dir)

# should print
# fortune
# gateway
# harvest
# capture

# Write a recursive function to print just the directories
def print_dirs(file):
    # what's the recursive case?
    # what's the base case (how do we know to stop recursing)?
    # when should we print?
    
    # if file.is_dir:
    #     print(file.name)
    # else:
    #     return
    # # It's a directory
    # for child in file.files:
    #     print_dirs(child)
    
    # or
    if not file.is_dir:
        return
    print(file.name)

    # It's a directory
    for child in file.files:
        print_dirs(child)
    

print("== print_dirs ==")
print_dirs(my_dir)

# should print
# root
# almonds
# default
# explore
# blanket
# journey

#
# CHALLENGING QUESTION
#############################

# Write a recursive function to print an indented view of the structure
# (indent by four spaces for each layer down in the structure)
def print_indented(file, depth=0):
    # what's the recursive case?
    # what's the base case (how do we know to stop recursing)?
    # how should we format the printing (using the depth)?
    # how do we update the depth passed in the parameters?

    # the following code can be used to build the indentation based on the depth
    # indent = "    " * depth
    
    



    pass

print("== print_indented ==")
print_indented(my_dir)

# should print
# root
#     almonds
#         default
#             fortune
#         explore
#             gateway
#     blanket
#         harvest
#         journey
#     capture

#
# SUPER ULTRA BONUS QUESTION
#############################

#
# SERIOUSLY, THIS IS TOUGH
#############################

#
# OK, YOU'VE BEEN WARNED
#############################

# Write a recursive function that duplicates the structure display from
# the top of the explanation
def print_tree(file, has_next=None):
    # has_next should track, at each level of indentation,
    # whether there is a next sibling,
    # which affects the glyphs used for indentation
    # for example, for "gateway", has_next should contain [True, False, False]

    # notice that while the logic for building up the indenting
    # patterns is more complex here, in the main, the way
    # we move through the directory structure is identical
    # to the simpler print_indented

    has_next = has_next or []  # init to new empty list if default

    depth = len(has_next)  # the length of the list indicates how deep we are in the hierarchy

    # how can we build up the symbols used to draw the lines
    # the following characters should be used: │ ├ ─ └
    # review their arrangement in the sample output below

    # what's the recursive case?
    # what's the base case (how do we know to stop recursing)?
    # how should we format the printing (using the depth)?
    # how do we update the depth passed in the parameters?

print("== print_tree ==")
print_tree(my_dir)

# should print
# root
# ├── almonds
# │   ├── default
# │   │   └── fortune
# │   └── explore
# │       └── gateway
# ├── blanket
# │   ├── harvest
# │   └── journey
# └── capture

#
# SUPER DUPER EXTRA CHALLENGE
##################################

# Research how to get actual file and directory information in
# Python, and build a little script to draw the above tree structure
# for some directory on your computer!

# (There's a terminal command called tree that does this that you can
# use for comparison! tree can be installed through homebrew.)

def dirtree(path, has_next=None):
    pass

print("== dirtree ==")
dirtree(".")
