"""QUESTION
Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]

And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]


____________________________________________________________________________________________________________
decided to put all my code evolution here
def tower_builder(n_floors):
    num = n_floors + 1  # Total levels including the base level
    i = 1  # Start with the first floor
    x = " "  # Space character for padding
    j = 1  # Increment for stars
    tower = []  # List to store each level of the tower
    
    while i < num:
        if i == 1:
            level = x * (n_floors - 1) + "*" * i
            tower.append(level)
            i += 1
        else:
            level = x * (n_floors - i) + "*" * (i + j)
            tower.append(level)
            i += 1
            j += 1

    return tower
result = tower_builder(6)
for floor in result:
    print(floor)
def tower_builder(n_floors):
    num = n_floors + 1  # Total levels including the base level
    i = 1  # Start with the first floor
    x = " "  # Space character for padding
    j = 1  # Increment for stars
    
    while i < num:
        if i == 1:
            print(x * (n_floors - 1), "*" * i)
            i += 1
        else:
            print(x * (n_floors - i), "*" * (i + j))
            i += 1
            j += 1


# build here
tower_builder(3)
tower_builder(6)
FINAL SOLUTION
"""
def tower_builder(n_floors):
    num = n_floors + 1  
    num2 = int(n_floors) 
    i = 1  
    x = " "  # Space character for balance of the pyramid :)
    j = 1  # Increment for stars
    tower = []  

    while i < num:
        if i == 1:
            level = x * (num2 - i) + "*" * i + x * (num2 - i)
            tower.append(level)
            i += 1
        else:
            level = x * (num2 - i) + "*" * (i + j) + x * (num2 - i)
            tower.append(level)
            i += 1
            j += 1

    return tower
