import sys
n = int(input().strip())
a= [int(a_temp) for a_temp in input().strip().split(' ')]
b= [int(a_temp) for a_temp in input().strip().split(' ')]
a=a[0:n]
b=b[0:n]
a.sort()
b.sort()
sum=0
for i in range(len(a)):
    sum+=abs(a[i]-b[i])
print(sum)

