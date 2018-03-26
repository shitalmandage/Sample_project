#http://www.geeksforgeeks.org/paper-cut-minimum-number-squares/
import sys
t=int(input().strip())
result=[]
for i in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    cnt=0
    while(m>0):
        if n>m:
            n,m=m,n
        cnt=cnt+1
        m=m-n
    result.append(cnt)
for r in result:
    print(r)


