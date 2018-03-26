#
s1=input().strip()
s2=input().strip()
s1=list(s1)
s2=list(s2)
cnt=[0]*len(s1)
string=['']*len(s1)
for i in range(len(s1)):
    for j=i in range(len(s2)):
        if s[i]==s2[j]:
            cnt[i]+=1
            break



