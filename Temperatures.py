import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
min = 5526
result=0
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    abst = t
    if t < 0:
        abst = -t
    if abst < min:
        min = abst
        result = i
    elif abst == min and t>0:
        min = abst
        result = i
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(result)
