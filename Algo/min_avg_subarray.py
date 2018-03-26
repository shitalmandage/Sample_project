import sys

def min_avg_sub_array(arr,k):
    if k<=len(arr):
        min_avg=int(sum(arr[:k])/k)
        sub_array=arr[:k]
        for i in range(1,len(arr)-k):
            avg=int(sum(arr[i:i+k])/k)
            if avg<min_avg:
                sub_array=arr[i:i+k]
                min_avg=avg
    return min_avg,sub_array

n,k=input().strip().split(' ')
n,k=[int(n),int(k)]
arr=[int(i) for i in input().strip().split(' ')]
result,sub_array=min_avg_sub_array(arr[:n],k)
print(result)
print(sub_array)
            
