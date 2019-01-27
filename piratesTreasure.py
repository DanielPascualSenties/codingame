import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = int(input())
h = int(input())
matrix = [[0 for x in range(w)] for y in range(h)] 
for i in range(h):
    k=0;
    for j in input().split():
        matrix[int(i)][k] = int(j)
        k=k+1;
        

for i in range(h):
    for j in range(w):
        if (matrix[int(i)][int(j)] == 1):
            #print(str(i)+','+str(j)+ ' is a 1, discarded')
            continue;
        if (int(i)!=0):
            if (int(j)!=0):
                if (matrix[int(i)-1][int(j)-1] == 0):
                    #print(str(i)+','+str(j)+ ':found 0 on the -1 -1')
                    continue;
            if (matrix[int(i)-1][int(j)] == 0):
                #print(str(i)+','+str(j)+ ':found 0 on the -1 +0')
                continue;
            if (int(j) != (w-1)):
                if (matrix[int(i)-1][int(j)+1] == 0):
                    #print(str(i)+','+str(j)+ ':found 0 on the -1 +1')
                    continue;
        if (int(j)!=0):
            if (matrix[int(i)][int(j)-1] == 0):
                #print(str(i)+','+str(j)+ ':found 0 on the +0 -1')
                continue;
        if (int(j)!=(w-1)):
            if (matrix[int(i)][int(j)+1] == 0):
                #print(str(i)+','+str(j)+ ':found 0 on the +0 +1')
                continue;
        if (int(i)!=(h-1)):
            if (int(j)!=0):
                if (matrix[int(i)+1][int(j)-1] == 0):
                    #print(str(i)+','+str(j)+ ':found 0 on the +1 -1')
                    continue;
            if (matrix[int(i)+1][int(j)] == 0):
                #print(str(i)+','+str(j)+ ':found 0 on the +1 +0')
                continue;
            if (int(j) != (w-1)):
                if (matrix[int(i)+1][int(j)+1] == 0):
                    #print(str(i)+','+str(j)+ ':found 0 on the +1 -1')
                    continue;     
        x,y =i,j;
        
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(str(y) +' '+ str(x))
