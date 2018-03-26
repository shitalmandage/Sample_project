def connect_ropes(ropes,sum):
    ropes.sort()
    s=ropes[0]+ropes[1]
    sum+=s
    ropes.pop(0)
    ropes[0]=s
    if len(ropes)==1:
        print(sum)
    else:
        connect_ropes(ropes,sum)
    

import sys
t = int(input().strip())
result=[]
for a0 in range(t):
    n=int(input().strip())
    ropes = [int(a_temp) for a_temp in input().strip().split(' ')]
    sum=0
    connect_ropes(ropes,sum)
