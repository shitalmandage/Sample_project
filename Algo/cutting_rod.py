def fun(n):
    l=[1,2,3,4,5,6,7,8]
    p=[1,5,8,9,10,17,17,20]
    solution=[]
    for i in range(len(l)):
        solution.append(0)
    sol=0
    if n==0:
        return 0
    else:
        for i in range(len(l)):
            if n>=l[i]:
                solution[i]=p[i]+fun(n-l[i])
                sol=max(sol,solution[i])
    return sol

n = int(input("enter len:"))
print ("max price=",fun(n))

