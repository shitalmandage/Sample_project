import sys

n=int(input().strip())
arr=[int(i) for i in input().strip().split(' ')]

x=arr[0]
for i in range(0,n-1):
    arr[i]=arr[i+1]

arr[-1]=x

print(arr)

