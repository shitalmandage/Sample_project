import sys

def reverse_block(arr,l ,m):
    while (l<m):
        arr[l],arr[m]=arr[m],arr[l]
        l+=1
        m-=1
    return arr

n=int(input().strip())
arr=[int(i) for i in input().strip().split(" ")]
start,end=input().strip().split(" ")
start, end=[int(start),int(end)]
arr=reverse_block(arr,start,end)
print(arr)
