"https://adventofcode.com/2015/day/2"

import os

os.system('cls')

f = open("input files\input2.txt","r")
file = f.readlines()
f.close()

wrapping_paper_total = 0 #sq ft
ribbon_total = 0 #ft

for box in file:

    first_x_pos = box.find("x")
    second_x_pos = box.find("x", first_x_pos + 1)

    length = int(box[0:first_x_pos])
    width = int(box[first_x_pos+1:second_x_pos])
    height = int(box[second_x_pos+1:len(box)])

    length_x_width = length*width
    length_x_height = length*height
    width_x_height = width*height

    perimeter_length_width = 2*length + 2*width
    perimeter_length_height = 2*length + 2*height
    perimeter_width_height = 2*width + 2*height

    #print(f"length: {length}     width: {width}     height: {height}")

    surface_area = 2*length_x_width + 2*length_x_height + 2*width_x_height
    volume = length * width * height

    wrapping_paper = surface_area + min([length_x_width, length_x_height, width_x_height])
    wrapping_paper_total += wrapping_paper

    ribbon = min([perimeter_length_width, perimeter_length_height, perimeter_width_height]) + volume
    ribbon_total += ribbon


print(f"The elves need {wrapping_paper_total} sq ft of wrapping paper and {ribbon_total} ft of ribbon")



