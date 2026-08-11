class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # nums.sort()
        # hmap={}
        p=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                p+=nums[i]
            else:
                break
        while(p in nums):
            p+=1
        return p
