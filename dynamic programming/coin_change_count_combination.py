def numWays(coins,tsum):
    if (tsum == 0):
        return 1
    if (tsum<0):
        return 0
    ways=0
    for g in range(len(coins)):
        tsum=tsum-coins[g]
        ways=ways+numWays(coins[g:],tsum)
        tsum=tsum+coins[g]
    return ways
coins=[1,2,3]
tsum=4
count=0
print(numWays(coins,tsum))