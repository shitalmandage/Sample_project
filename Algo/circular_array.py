#code
#http://www.geeksforgeeks.org/maximize-sum-consecutive-differences-circular-array/
import sys 
t=int(input().strip())
result=[]
for i in range(t):
    n=int(input().strip())
    arr=[int(i) for i in input().strip().split(' ')]
    arr=arr[0:n]
    arr.sort()
    half_len=int(n/2)
    a=arr[0:half_len]
    b=arr[half_len:n]
    list.reverse(b)
    #print(a)
    #print(b)
    j=0
    for i in range(len(a)):
        arr[j]=a[i]
        arr[j+1]=b[i]
        j=j+2
    if len(b)>len(a):
        arr[-1]=b[-1]
    #print(arr)
    sum=0
    for i in range(n):
        if i==(n-1):
            sum+=abs(arr[i]-arr[0])
        else:
            sum+=abs(arr[i]-arr[i+1])
    result.append(sum)
for r in result:
    print(r)

    
