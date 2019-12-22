def lcs(s1,s2,m,n,memo):
    if(m==0 or n==0):
        return 0
    if(memo[m-1][n-1]!=-1):
        return memo[m-1][n-1]
    if(s1[m-1]==s2[n-1]):
        memo[m-1][n-1]=1+lcs(s1,s2,m-1,n-1,memo)
        return memo[m-1][n-1]
    else:
        memo[m-1][n-1]=max(lcs(s1,s2,m-1,n,memo),lcs(s1,s2,m,n-1,memo))
        return memo[m-1][n-1]
s1="axyzgnq"
s2="bazgnqx"
memo=[[-1 for g in range(len(s2))] for b in range(len(s1))]
print(lcs(s1,s2,len(s1),len(s2),memo))