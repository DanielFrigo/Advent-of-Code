"https://adventofcode.com/2015/day/3"

#Things to do:
#Figure out a more efficient way to copy a 2d list

import os
import copy

os.system('cls')

class Santa:

    def __init__(self, pos_x, pos_y, robot=False):
        self.x = pos_x
        self.y = pos_y
        self.robot = robot

    def move(self, instr):
        if instr == ">":
            self.x += 1
        elif instr == "<":
            self.x -= 1
        elif instr == "^":
            self.y += 1
        elif instr == "v":
            self.y -= 1

    def place(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

f = open("input files\input3.txt","r")
file = f.read()
f.close()

#initialize a grid of houses with no presents delivered "0"
#We do not need to check more houses then there are instructions in the file.
#we'll put santa in the center and ensure he has sufficient space to go west, east, north, or south

#there's probabbly a more efficient way to copy grid1 onto grid2
grid1 = [[0 for i in range(2*len(file))] for j in range(2*len(file))]
grid2 = [[0 for i in range(2*len(file))] for j in range(2*len(file))]
    

houses_visited = 1 #starting house

#put santa in the middle
center_x = len(file)
center_y = center_x

santa = Santa(center_x, center_y)
robot = Santa(center_x, center_y, robot=True)

grid1[santa.x][santa.y] = 1 #present delivered
grid2[santa.x][santa.y] = 1 #present delivered

for instr in file:
    santa.move(instr)

    if grid1[santa.x][santa.y] == 0:
        
        grid1[santa.x][santa.y] = 1
        houses_visited += 1

print(f"Presents delivered to {houses_visited} houses in year 1")

santa.place(center_x, center_y)

santa_moves = True
robot_moves = False

houses_visited = 1 #starting house

for instr in file:

    if (santa_moves):
        santa.move(instr)

        if grid2[santa.x][santa.y] == 0:
            grid2[santa.x][santa.y] = 1
            houses_visited += 1

        santa_moves = False
        robot_moves = True

    else:
        robot.move(instr)

        if grid2[robot.x][robot.y] == 0:
            grid2[robot.x][robot.y] = 1
            houses_visited += 1

        santa_moves = True
        robot_moves = False

print(f"Presents delivered to {houses_visited} houses in year 2\n")