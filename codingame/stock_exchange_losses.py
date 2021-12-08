import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
stock_vals = [int(val) for val in input().split()]

if len(stock_vals) >= 2 :
    max_loss = stock_vals[1] - stock_vals[0]
    max_val = stock_vals[0]

    for i in range(len(stock_vals)):
        if max_loss > stock_vals[i] - max_val :
            max_loss = stock_vals[i] - max_val
        if stock_vals[i] > max_val :
            max_val = stock_vals[i]
            
else : max_loss = 0
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(max_loss)
