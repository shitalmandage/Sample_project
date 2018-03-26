#L=[3,2,-10,5,8,-30,7]
#L=[3,2,-10,5,8,2,-30,7,8,9]
L=[3,2,-10,5,8,2,10,-30,7,8,9]
S=[]
A=[]
for i in range(len(L)):
    S.append(L[i])
for i in range(len(L)):
    A.append(i)
for i in range(1,len(L)):
    for j in range(i):
        if (L[i]<(L[i]+S[i-1])):
            A[i]=i-1
        S[i]=max(L[i],L[i]+S[i-1])
#print (L)
#print (S)
#print (A)
n=max(S)
ind=S.index(n)
R=[]
#print(ind)
m=A[ind]
for i in range(m):
    R.append(L[ind])
    if (A[ind]==ind):
        print (list(reversed(R)))
        exit()
    else:
        ind=A[ind]
