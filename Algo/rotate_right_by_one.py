import sys

n=int(input().strip())
arr=[int(i) for i in input().strip().split(' ')]

x= arr[-1]
for i in range(n-1,-1,-1):
    arr[i]=arr[i-1]

arr[0]=x
print(arr)
