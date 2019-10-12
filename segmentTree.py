class Node:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.total=0
        self.left=None
        self.right=None

class NumArray(object):
    def __init__(self,nums):
        self.root=self.createTree(nums,0,len(nums)-1)

    def createTree(self,nums,l,r):
        if(l==r):
            n=Node(l,r)
            n.total=nums[l]
            return n

        mid=(l+r)//2

        root=Node(l,r)

        root.left=self.createTree(nums,l,mid)
        root.right=self.createTree(nums,mid+1,r)

        root.total=root.left.total+root.right.total

        return root

    def sumRange(self,i,j):
        def rangeSum(root,i,j):
            if(root.start==i and root.end==j):
                return root.total

            mid=(root.start+root.end)//2

            if(j<=mid):
                return rangeSum(root.left,i,j)
            elif(i>=mid+1):
                return rangeSum(root.right,i,j)
            else:
                return rangeSum(root.left,i,mid)+rangeSum(root.right,mid+1,j)

        return rangeSum(self.root,i,j)
nums=[1,4,5,6,7,8]
numArray=NumArray(nums)
print(numArray.sumRange(0,1))
print(numArray.sumRange(1,2))
print(numArray.sumRange(4,5))
print(numArray.sumRange(5,5))
