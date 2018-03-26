#http://www.geeksforgeeks.org/longest-repeated-subsequence/
import sys
string=input().strip()
s=string
mydict={}
key=[]
value=[]
while len(string)!=0:
    ch=string[0]
    key.append(ch)
    value.append(string.count(ch))
    string=string.replace(ch,'')
print(key)
print(value)
s=''
for i in range(len(value)):
    if value[i]>=2:
        s=s+(key[i])
print(s)


