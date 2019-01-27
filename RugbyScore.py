import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
maxtries = n // 5
for i in range(maxtries+1):
    pointsaftertries = n - 5*int(i)
    #print(pointsaftertries,file=sys.stderr)
    maxconversions = min(pointsaftertries//2, i);
    for j in range(maxconversions+1):
        pointsafterconversions = pointsaftertries - 2*int(j);
        #print(pointsafterconversions,file=sys.stderr)
        maxpenalties = pointsafterconversions // 3
        for k in range(maxpenalties+1):
            pointsafterpenalties= pointsafterconversions - 3*int(k)
            if (pointsafterpenalties == 0):
                print(str(i)+' '+str(j)+' '+str(k));
