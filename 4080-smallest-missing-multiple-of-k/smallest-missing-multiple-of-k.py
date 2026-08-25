class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        h=set(nums)
        while True:
            if i*k not in h:
                return i*k
            i+=1
            