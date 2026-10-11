class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n=len(numbers)
        hmap={}
        for i in range(n):
            c=target-numbers[i]
            if c in hmap:
                return[hmap[c]+1,i+1]
            hmap[numbers[i]]=i
        return[-1,-1]        