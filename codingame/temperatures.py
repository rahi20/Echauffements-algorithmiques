import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

result = 0
first = True
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if first : 
        result = t
        first = False
    if abs(t) < abs(result) : result = t
    elif abs(t) == abs(result) and t > result : result = t 

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)
