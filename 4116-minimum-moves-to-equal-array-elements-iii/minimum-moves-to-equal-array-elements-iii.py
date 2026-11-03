class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        l=[]
        for i in nums:
            l.append(abs(m-i))
        return sum(l)