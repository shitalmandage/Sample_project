#L=[3,5,1,9,8,2,7,5,13,16,12]
L=[3,5,1,9,8,2,7,5,13,6,12]
A=[]
S=[]
# S=[1 for x in L]
for i in range(len(L)):
    S.append(1)

for i in range(len(L)):
    A.append(i)

def LIS(L,S):
    for i in range(len(S)):
        for j in range(i):
            if L[i]>=L[j] and S[i]<=S[j]:
                S[i]=1+S[j]
                A[i]=j
    #print (L)
    #print (S)
    #print (A)
    n=max(S)
    #print (n)
    ind=S.index(n)
    #print (ind)
    R=[]
    for i in range(n):
        R.append(L[ind])
        ind=A[ind]
    print ("longest increasing sublist is : ", list(reversed(R)))



LIS(L,S)

