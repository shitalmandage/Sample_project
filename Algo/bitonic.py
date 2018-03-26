#           7 2 9 5 1 8 6 5 11 2 8 
#SL         1 1 2 2 1 3 3 2 4  2 4
#SR         4 2 5 2 1 4 3 2 2  1 1
#max SL+SR  5 3 7 4 2 7 6 4 6  3 5


A=[7,2,9,5,1,8,6,5,11,2,8]
SLeft=[]
SRight=[]
pick_left=[]
pick_right=[]
Add_SL_SR=[]
for i in range(len(A)):
    SLeft.append(1)
    SRight.append(1)
    Add_SL_SR.append(0)
    pick_left.append(i)
    pick_right.append(i)

def LIS(A,SLeft,pick_left):
    for i in range(len(A)):
        for j in range(i):
            if A[i]>=A[j] and SLeft[i]<=SLeft[j]:
                SLeft[i]=1+SLeft[j]
                pick_left[i]=j
    n=max(SLeft)
    ind=SLeft.index(n)
    R=[]
    for i in range(n):
        R.append(A[ind])
        ind=pick_left[ind]
    return list(reversed(R))

def LDS(A,SRight,pick_right):
    for i in range(len(A)):
        for j in range(i):
            if A[i]<=A[j] and SRight[i]>=SRight[j]:
                SRight[i]=1+SRight[j]
                pick_right[i]=j
    n=max(SRight)
    ind=SRight.index(n)
    R=[]
    for i in range(n):
        R.append(A[ind])
        ind=pick_right[ind]
    return list(reversed(R))

R_LIS=LIS(A,SLeft,pick_left)
print (R_LIS)

R_LDS=LDS(list(reversed(A)),SRight,pick_right)
print (R_LDS)
