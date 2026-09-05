class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        rmin,lmax=min(nums),nums[0]
        ssi=-1
        premax=[nums[0]]+[0]*(n-1)
        sufmin=[0]*(n-1)+ [nums[-1]]
        for i in range(1,n):
            premax[i]=max(premax[i-1],nums[i])
        for i in range(n-2,-1,-1):
            sufmin[i]=min(sufmin[i+1],nums[i])
        for i in range(n):
            if premax[i]-sufmin[i] <= k:
                ssi=i
                break
        return ssi