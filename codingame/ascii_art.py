import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
rows = []

init = ord("A")
ascii = []

for i in range(h):
    row = input()
    line = ""
    for c in list(t) : 
        diff = ord(c.upper()) - init
        if diff > (ord("Z") - init) or diff < 0 :
            line += row[-1-(l-1):] 
            continue
        line += row[diff * l : diff * l + l]
    ascii.append(line)

for line in ascii:
    print(line)
