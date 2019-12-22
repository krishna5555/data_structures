import time
def maxCuts(n,ls,count,rs):
    if(memo.get(n) is not None):
        return memo[n]
    if(n==0):
        return 1
    if(n<0):
        return 0
    for g in range(len(ls)):
        if(maxCuts(n-ls[g],ls[g:],count+1,rs)==1):
            if(count>rs[-1]):
                rs[-1]=count
        memo[n]=rs[-1]
    return
memo={}
n=5
ls=[1,2,3,4]
rs=[-1]
count=0
start=time.time()
maxCuts(n,ls,count,rs)
end=time.time()
if(rs[-1]!=-1):
    print(rs[-1]+1)
else:
    print(-1)
print(end-start)