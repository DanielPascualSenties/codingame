import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    l=[0,0,0,0,0,0,0,0]
    card = input();
    l[0] = int(card[17]);
    l[1] = int(card[15]);
    l[2] = int(card[12]);
    l[3] = int(card[10]);
    l[4] = int(card[7]);
    l[5] = int(card[5]);
    l[6] = int(card[2]);
    l[7] = int(card[0]);
    for i in range(8):
        l[i] = 2*l[i]
        if (l[i]>9):
            l[i]=l[i]-9;
    ltotal = 0;
    for i in range(8):
        ltotal = ltotal + l[i];
    r=[0,0,0,0,0,0,0,0]
    r[0] = int(card[18]);
    r[1] = int(card[16]);
    r[2] = int(card[13]);
    r[3] = int(card[11]);
    r[4] = int(card[8]);
    r[5] = int(card[6]);
    r[6] = int(card[3]);
    r[7] = int(card[1]);
    rtotal = 0;
    for i in range(8):
        rtotal = rtotal + r[i];
    print(ltotal,file=sys.stderr)
    print(rtotal,file=sys.stderr)
    total = rtotal + ltotal;
    if (total%10==0):
        print("YES");
    else: 
        print("NO");

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(l, file=sys.stderr)
