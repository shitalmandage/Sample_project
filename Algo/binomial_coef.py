# A naive recursive Python implementation
 
def binomialCoeff(n , k):
 
    if k==0 or k ==n :
        return 1
 
    # Recursive Call
    return binomialCoeff(n-1 , k-1) + binomialCoeff(n-1 , k)
 
# Driver Program to test ht above function
n = 5
k = 2
print "Value of C(%d,%d) is (%d)" %(n , k , binomialCoeff(n , k))
 
# This code is contributed by Nikhil Kumar Singh (nickzuck_007)





#################################################################

# A Dynamic Programming based Python Program that uses table C[][]
# to calculate the Binomial Coefficient
 
# Returns value of Binomial Coefficient C(n, k)
def binomialCoef(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]
 
    # Calculate value of Binomial Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
 
            # Calculate value using previosly stored values
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
 
    return C[n][k]
 
# Driver program to test above function
n = 5
k = 2
print("Value of C[" + str(n) + "][" + str(k) + "] is "
      + str(binomialCoef(n,k)))
