import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
lines = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    lines.append(list(line))

for y in range(height):
    for x in range(width):
        if lines[y][x] == ".":
            continue

        rx = ry = bx = by = -1
        #check right neighbor
        if (x + 1) <= (width - 1) :
            for i in range(x+1, width):
                if lines[y][i] == "0":
                    rx = i
                    ry = y
                    break
        #if (x + 1) <= (width - 1) and lines[y][x + 1] == "0" :
        #    rx = x + 1
        #    ry = y

        #check for bottom neighbor
        if (y + 1) <= (height - 1) :
            for j in range(y+1, height):
                if lines[j][x] == "0":
                    bx = x
                    by = j
                    break

        #if (y + 1) <= (height - 1) and lines[y + 1][x] == "0" :
        #    bx = x
        #    by = y + 1
        
        print("{0} {1} {2} {3} {4} {5}".format(x, y, rx, ry, bx, by))

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Three coordinates: a node, its right neighbor, its bottom neighbor
#print("0 0 1 0 0 1")
