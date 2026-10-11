
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        l = r = 0
        minsize = float('inf')
        psums = 0

        while r < n:
            psums += nums[r]
            r += 1

            while psums >= target:
                minsize = min(minsize, r - l)
                psums -= nums[l]
                l += 1

        return 0 if minsize == float('inf') else minsize
