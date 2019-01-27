import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def distance(x1,y1,x2,y2):
    xdist = (x1-x2)**2
    print(str(xdist))
    ydist = (y1-y2)**2
    dist = xdist + ydist
    dist = math.sqrt(dist)
    return dist

# print(str(distance(0,0,3,4)), file=sys.stderr)
n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("distance")
