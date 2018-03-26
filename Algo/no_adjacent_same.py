#http://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/
import sys
string=input().strip()
s=string
mydict={}
while len(string)!=0:
    ch=string[0]
    mydict[ch]=string.count(ch)
    string=string.replace(ch,'')
print(mydict)
m=max(mydict.values())
sum=0
for key, value in mydict.items():
    sum+=value
sum=sum-m
print(sum)
if m>sum:
    print("Not Possible")
else:
    ''' 
    string=list(s)
    j=0
    for i in range(len(a)):
        s[j]=
        s[j+1]=b[i]
        j=j+2
    if len(b)>len(a):
        arr[-1]=b[-1]
