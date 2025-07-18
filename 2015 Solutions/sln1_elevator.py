"https://adventofcode.com/2015/day/1"

import os

os.system('cls')

f = open("input files\input1.txt","r")
file = f.read()
f.close()

floor = 0
basement_entered = False
first_basement_entry = 0
char_position = 1

for instr in file:

    if instr == "(":
        floor += 1
    elif instr == ")":
        floor -= 1
    if floor < 0 and basement_entered == False:
        basement_entered = True
        first_basement_entry = char_position
    
    char_position += 1

print(f"Santa should go to floor {floor}\n")
print(f"He first entered the basement at position {first_basement_entry}\n")


