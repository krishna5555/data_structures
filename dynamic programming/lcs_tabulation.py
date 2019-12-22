def lcs(s1,s2,m,n,memo):
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                memo[i][j]==0
            elif(s1[i-1]==s2[j-1]):
                memo[i][j]=1+memo[i-1][j-1]
            else:
                memo[i][j]=max(memo[i-1][j],memo[i][j-1])
    return memo[m][n]
s1="axyzgnq"
s2="bazgnqx"
memo=[[0 for g in range(len(s2)+1)] for b in range(len(s1)+1)]
print(lcs(s1,s2,len(s1),len(s2),memo))