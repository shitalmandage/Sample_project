import sys

def reverse_block(arr,n ,m):
    m=m%n
    i=0
    k=m-1
    while (i<k):
        arr[i],arr[k]=arr[k],arr[i]
        i+=1
        k-=1
    i=m
    k=n-1
    while (i<k):
        arr[i],arr[k]=arr[k],arr[i]
        i+=1
        k-=1
    i=0
    k=n-1
    while (i<k):
        arr[i],arr[k]=arr[k],arr[i]
        i+=1
        k-=1
    return arr
t=int(input().strip())
result=[]
for i in range(t):
    n,m=input().strip().split(" ")
    n, m=[int(n),int(m)]
    arr=[int(i) for i in input().strip().split(" ")]
    result.append(reverse_block(arr,n,m))

for r in result:
    print(" ".join(map(str,r)))
