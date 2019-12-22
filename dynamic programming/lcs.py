def lcs(s1,s2,m,n):
    if(m==0 or n==0):
        return 0
    if(s1[m-1]==s2[n-1]):
        return 1+lcs(s1,s2,m-1,n-1)
    else:
        return max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
s1="axyzgnq"
s2="bazgnqx"
print(lcs(s1,s2,len(s1),len(s2)))