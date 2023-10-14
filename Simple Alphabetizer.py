# Simple Alphabetizer
# Python 3.9.6
# A program by Tyler Serio
# This program takes a line by line list of words and alphabetizes them

filename = "your_file_name.txt" # Change this to whatever your file's name is
file = open(filename, "r")
newfile = open("your_new_file.txt", "w")
linelist = []
x = -1
for line in file:
    x += 1
    linelist.append(line)
finalline = linelist.pop(x)
linelist.append(finalline + "\n")
linelist = sorted(linelist)
finalline = linelist.pop(x)
linelist.append(finalline.strip("\n"))
for x in linelist:
    newfile.write(x)
file.close()
newfile.close()
