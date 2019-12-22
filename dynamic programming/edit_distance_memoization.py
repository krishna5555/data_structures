import time
def editDist(s1,s2,m,n,memo):
    if(memo.get(s1+s2) is not None):
        return memo[s1+s2]
    if(m==0):
        return n
    elif(n==0):
        return m
    if(s1[m-1]==s2[n-1]):
        memo[s1+s2]=editDist(s1,s2,m-1,n-1,memo)
        return memo[s1+s2]
    else:
        memo[s1+s2]=1+min(editDist(s1,s2,m-1,n-1,memo),editDist(s1,s2,m-1,n,memo),editDist(s1,s2,m,n-1,memo))
        return memo[s1+s2]
memo={}
s1="text"
s2="txtngq"
start=time.time()
print(editDist(s1,s2,len(s1),len(s2),memo))
end=time.time()
print(end-start)