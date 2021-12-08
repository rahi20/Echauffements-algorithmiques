import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]


r = w - 1
l = 0
b = h - 1
t = 0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)


    if "U" in bomb_dir : 
        b = y0 - 1
    elif "D" in bomb_dir : 
        t = y0 + 1

    if "R" in bomb_dir :
        l = x0 + 1
    elif "L" in bomb_dir : 
        r = x0 - 1
    
    x0 = l + (r - l) // 2
    y0 = t + (b - t) //2

    print("{0} {1}".format(x0, y0))