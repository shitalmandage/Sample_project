import sys
coins=[1, 2, 5, 10, 20, 50, 100, 500, 1000]
list.reverse(coins)
print("enter how may rs")
n = int(input().strip())
rs=n
c=[]
cnt=0
while(n!=0):
    for i in range(len(coins)):
        if n>=coins[i]:
            n=n-coins[i]
            c.append(coins[i])
            cnt=cnt+1
            #coins=coins[:(coins.index(coins[i])+1)]
            break;
        
print(n,rs,c,cnt)

    
