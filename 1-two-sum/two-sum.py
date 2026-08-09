class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dect = {}
        for i in range(n):
            rem = target - nums[i]
            if rem in dect:
                return[dect[rem],i]
            dect[nums[i]] = i
            